---
layout: base
title: "Building a Python parallel processing pipeline package (R-3PO)"
date: 2020-08-29
tags:
  - programming
  - build
  - public
  - internship
  - inzura
permalink: "/{{ page.date | date: '%Y/%m/%d' }}/{{page.fileSlug}}/"
---

<div class = "toc">

[[toc]]

</div>

## Introduction

Richard Jelbert (CEO of Inzura) and I whipped up
a Python parallel processing pipeline package
(just rolls off the tongue, doesn't it) over a couple of days.
We used it to process a large number (over 3 million) of JSON files.

**Richard's Parallel Processing Protocol**, or R-3PO for short (like C-3PO)
is an embarassingly
trivial package built on top of [Ray](https://github.com/ray-project/ray)
to make embarassingly parallel problems embarassingly easy.

Use case: Suppose you have lots of data files that
need to be processed in the exact same way with the same function.
And suppose you want to save the results of that processing into a CSV file.
This is an _embarassingly parallel_ problem: it should be easy.

_Embarassingly_ easy, even: R3PO lets you do it with a `config.yaml`
file and two lines of code. It automatically
handles the distribution of tasks to processes,
saves your progress so you can stop and restart the job anytime,
and logs all errors automatically.

This package is probably useless to you unless your
workflow and use case are very similar to mine.
But if it is, I believe it could save you an hour or two
from needing to write boilerplate code.

---

## 1 minute guide

Have the following two files in your directory.

`config.yaml`:

```yaml
job_name: count_produce
processes: 2
source_path: /home/lieu/produce_log
source_file_part: .json
working_dir: /home/lieu/working_dir
output_path: /home/lieu/output_dir
```

`main.py`:

```python
# main.py

from r3po import jobbuilder, jobrunner
from count_fruits import count_fruits

# Build jobs
build_jobs('./config.yaml')

# Now run them
run_jobs('./config.yaml', count_fruits)
```

Running `python3 main.py` will run the `count_fruits` function on all `.json`
files in `/home/lieu/produce_log/` and log the results in numbered csv files
inside `/home/lieu/output_dir/`.

Sounds like something you'd find useful? Read on...

## Quickstart guide

We'll work though a very simple example available on the [Github repo](https://github.com/lieuzhenghong/r3po).
First, let's clone the repo and go to the `sample` directory:

### Cloning the repo

```bash
git clone https://github.com/lieuzhenghong/r3po
cd r3po/sample
```

The directory will look like this:

```python
./r3po/sample/
├── produce_log/
    ├── file_0.json
    ├── file_1.json
    ├── file_2.json
    ├── file_3.json
    ├── file_4.json
    ├── file_5.json
├── config.yaml
├── count_fruits.py
├── main.py
```

### Setting the scene

Imagine you're the king of Cornucopia and you own
one bajillion acres of land. You've allocated an acre of land to each one of your
loyal subjects for them to farm as they see fit.

One day, you decide that you'd like to know how much food is produced in Cornucopia.
So you ask your subjects to report their yields.
Your subjects are well-acquainted with both farming and the JSON spec,
so let's take a look at `file_0.json`:

```json
{
  "produce": {
    "fruits": {
      "apples": 24,
      "bananas": 33,
      "cantaloupes": 3
    },
    "vegetables": {
      "carrots": 15,
      "cucumbers": 22,
      "cabbages": 21
    },
    "meat": {
      "beef": 12,
      "pork": 2
    }
  }
}
```

Now as the king you're not that interested in the various types of fruits
per se---perhaps you only want the total sum of each type of produce.
Let's say you want something like the following:

```python
{
    "fruits": 60,
    "vegetables": 58,
    "meat": 14,
}
```

So you write a simple function that does exactly that.
The details are not important, but
**the key is that any such function must take in a filepath string and return a dictionary** for R3PO to work with it.

```python
# count_fruits.py
import json

def count_fruits(produce_log_filepath):
    with open(produce_log_filepath, 'r') as f:
        produce_counts = {}
        data = dict(json.load(f))
        all_produce = data['produce']
        for produce_type in all_produce:
            produce_counts[produce_type] = 0
            for produce in all_produce[produce_type]:
                produce_counts[produce_type] += int(
                    all_produce[produce_type][produce])
        return produce_counts

```

So you'd want to run this function for every file.
However, you have a bajillion acres of
land and thus a bajillion JSON files
(instead of the six files in the sample folder)
and so we'd like to speed it up by running the code in parallel.
Let's see how to do it with the R-3PO pipeline.

First, let's open `config.yaml` and take a look at the file.

```yaml
job_name: count_produce
processes: 2
source_path: /home/lieu/produce_log
source_file_part: .json
working_dir: /home/lieu/working_dir
output_path: /home/lieu/output_dir
```

Most of these are pretty self-explanatory (more details later),
but basically this means that

1. R3PO will spin up two parallel processes,
2. look for any file ending with `.json` in `/home/lieu/produce_log/`,
   and
3. write the results in `/home/lieu/output_dir`.

Now let's open the `main.py` file and see what's in it
(a whopping two lines of code):

```python
# main.py

from r3po import jobbuilder, jobrunner
from count_fruits import count_fruits

# Build jobs
build_jobs('./config.yaml')

# Now run them
run_jobs('./config.yaml', count_fruits)
```

Not much to say about this. Let's run it and see what happens:

### Running the code

```bash
# bash pip3 install r3po
# python3 main.py

Building job called: count_produce
Reading job source directory and generating master job CSV file...
Scanning for files ending with .json
Pending files generated.
Removing old node jobfiles...
Writing new node jobfiles...
Number of files: 6
Number of pending files: 6
2020-08-30 16:38:05,916 INFO resource_spec.py:223 -- Starting Ray with 5.47 GiB memory available for workers and up to 2.73 GiB for objects. You can adjust these settings with ray.init(memory=<bytes>, object_store_memory=<bytes>).
2020-08-30 16:38:06,302 INFO services.py:1191 -- View the Ray dashboard at localhost:8265
Spinning up Ray processes...
Process 0 spawned!
Process 1 spawned!
None
None
(pid=336291) Processed trip /home/lieu/dev/r3po/sample/output_dir/0.results.csv in node 0.
(pid=336291) Processed trip /home/lieu/dev/r3po/sample/output_dir/0.results.csv in node 0.
(pid=336291) Processed trip /home/lieu/dev/r3po/sample/output_dir/0.results.csv in node 0.
(pid=336283) Processed trip /home/lieu/dev/r3po/sample/output_dir/1.results.csv in node 1.
(pid=336283) Processed trip /home/lieu/dev/r3po/sample/output_dir/1.results.csv in node 1.
(pid=336283) Processed trip /home/lieu/dev/r3po/sample/output_dir/1.results.csv in node 1.
```

Okay, everything looks good! Let's take a look at
what has happened. There were a lot of print statements
which are self-explanatory.

We can see that Ray has spun up
two parallel processes
(exactly what we specified in the config.yaml file).
Additionally,
we can see that R3PO has created an output_dir with
two `results.csv` files.

We also have a `working_dir/` with `done.job` and
`nodejobfile.txt` files, but we won't worry about that for now.

```python
./r3po/sample/
├── output_dir/
    ├── 0.results.csv
    ├── 1.results.csv
├── produce_log/
    ├── file_0.json
    ├── file_1.json
    ├── file_2.json
    ├── file_3.json
    ├── file_4.json
    ├── file_5.json
├── working_dir/
    └── tracking/
        └── ..../file_0.json
            └── done.job
        └── ..../file_1.json
            └── done.job
        └── ..../file_2.json
            └── done.job
        └── ..../file_3.json
            └── done.job
        └── ..../file_4.json
            └── done.job
        └── ..../file_5.json
            └── done.job
    ├── 0.nodejobfile.txt
    ├── 1.nodejobfile.txt
├── config.yaml
├── count_fruits.py
├── main.py
```

Opening up the two `results.csv` files,
we can see that the function has
indeed been calculated for all of the input JSON files.
Because we spun up two processes, there are two
`results.csv` files:

```python
# 0.results.csv
fruits,vegetables,meat
60,58,14
3939,58,14
6456,3743,14
```

```python
# 1.results.csv
fruits,vegetables,meat
21,1539,79
60,58,14
5666,15,15
```

And we're done! These CSVs can then be converted
and concatenated with pandas's `pd.concat` function
to get pandas `DataFrames`,
which is the format in which I do the majority of my data analysis.

## How it works in more detail

### Overall abstraction

This pipeline runs a function `f` on a large number of
input files in parallel and logs the results into a CSV.

It is made up of two files.
The first file `jobbuilder.py` reads the `source_path` from `config.yaml`.
It looks for all files inside `source_path` that match a user-specified criteria.
It writes these file paths inside `nodejobfile` text files that tell each process
which files to work on.

The second file `jobrunner.py` spins up the processes.
Each process looks at its `nodejobfile` text file, and works through the list.

For each `$FILEPATH` listed in `nodejobfile`:

- the process opens the file,
- runs some function `f` on that file,
- and (tries to) append the output to a .csv file.

If the function successfully runs, an empty file called `done.job`
is created in `<$WORKING_DIR>/tracking/<$FILEPATH>/`as a record of completion.
If the function throws an exception, then a file called `error.job`
is created instead.

Keeping a record of file completion means that
the processes can be terminated and restarted at any time
without going through the same files again.

### Limitations and requirements

The pipeline requires the following to work:

1. A `config.yaml` file that follows a particular specification
2. A function that follows a specific contract (see next section)
3. All your input files must end with the same suffix.

#### The function contract

1. The function you call must take as input an absolute filepath to the file.
2. It must return a Dictionary that will be passed to
   [`csv.DictWriter`](https://docs.python.org/3/library/csv.html#csv.writer).
3. Furthermore, every Dictionary object returned **must have the same keys**.
   If it is not able to return such a Dictionary, it must raise an `Exception`.

#### The `config.yaml` file

This is what a config.yaml file should looks like. All fields are required.

```yaml
job_name: generate-trip-visualisations
output_path: /home/lieu/RJ/trip_processing_research/.generate-trip-visualisations
processes: 12
source_file_part: formatted.lz4
source_path: /media/lieu/bigdata/anonymous/rjrun
working_dir: /home/lieu/RJ/trip_processing_research/.generate-trip-visualisations
```

`count_all_files` and `count_job_files` are added by the program
and list the number of files in the job and the number of files remaining
in the job respectively.

`job_name` is the name of the processing job. It is used in
`print` statements only.

`processes` is the number of parallel processes to spin up.

`source_path` is a filepath string pointing to the folder where
the source files are.
`source_file_part` is used for filepath matching:
R3PO will traverse all subfolders inside `source_path`
and find all the `.json` files. In this case,

`working_dir` is a filepath string that points to a folder
to store intermediate files.
where the nodejobtxts will be, as well as the `done.job`
and `error.job` files.

`output_path` is a filepath string that points to a folder
where you want the results of the computations to
be written to CSV files. If the folder does not exist,
one will be automatically created.

#### What jobbuilder.py does

The jobbuilder module is responsible for getting the filepaths of all the
input files and
writing these filepaths to a CSV that jobrunner can read later.
It does not write the filepath if the file has already been processed
or if an error occurred whilst processing that file.

This is how it does it:

1. Read config.yaml file and find `source_path`, `working_dir`, and
   `source_file_part`
2. Create the folder `working_dir` if one does not exist
3. Look for file paths that match `source_path/**/*.source_file_part`,
   and do not already have a `done.job` or `error.job`
4. Write `X.nodejobfile.txt` by dividing the file paths up equally
   across all X process nodejobfiles

## Why does this even exist?

Admittedly, the code is pretty trivial, and quite overfitted to my specific
use-case. Why did I even bother packaging it up in the first place?
I offer three reasons:

1. If you think about it, the code is not _that_ trivial.
   It's easy enough to parallelise code in Python with the `multiprocessing`
   library. But it can be tricky to write code that allows jobs to terminate
   and restart arbitrarily, while not reprocessing already-processed files.
2. It follows from point 1 that
   this package will save you spending an hour or two reinventing the wheel
   if your use-case and dataflow are similar to mine.
3. I was lazy and wanted to be able to `pip install` rather than `git clone`-ing
   and moving the files around manually.

## Conclusion

Thanks for reading!
