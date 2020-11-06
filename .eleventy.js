const markdownIt = require("markdown-it");
const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");
const pluginRss = require("@11ty/eleventy-plugin-rss");

module.exports = function (eleventyConfig) {

  let markdownIt = require("markdown-it");
  /*  include extra functionality to the markdown parser */
  let markdownItFootnote = require("markdown-it-footnote");
  let markdownItAnchor = require("markdown-it-anchor");
  let markdownItToc = require("markdown-it-toc-done-right");
  let markdownItKatex = require("@iktakahiro/markdown-it-katex");

  const options = {
    html: true,
  };

  /* add stuff to the markdown parser */
  const markdownLib = markdownIt(options)
    .use(markdownItFootnote)
    .use(markdownItAnchor)
    .use(markdownItToc)
    .use(markdownItKatex);

  eleventyConfig.setLibrary("md", markdownLib);

  /* Parse markdown snippets inside {% markdown %} tags */
  eleventyConfig.addPairedShortcode("markdown", (content) => {
    //return md.render(content);
    return markdownLib.render(content);
  });

  // add syntax highlighting plugin
  // https://www.11ty.dev/docs/plugins/syntaxhighlight/
  eleventyConfig.addPlugin(syntaxHighlight);

  // add RSS plugin: https://www.11ty.dev/docs/plugins/rss/
  eleventyConfig.addPlugin(pluginRss);

  // returns an array of post years given a collection of posts
  eleventyConfig.addFilter("getYears", function (collection) {
    let years = [];
    collection.map((post) => {
      years.push(post.date.getFullYear());
    });
    return new Set(years.reverse());
  });

  // {{ array | year: value }}
  eleventyConfig.addFilter("year", function (array, value) {
    return array.filter((item) => {
      return item.date.getFullYear() === value ? item : false;
    });
  });

  // {{ array | where: key,value }}
  eleventyConfig.addFilter("where", function (array, key, value) {
    return array.filter((item) => {
      const keys = key.split(".");
      const reducedKey = keys.reduce((object, key) => {
        return object[key];
      }, item);

      return reducedKey === value ? item : false;
    });
  });

  eleventyConfig.addPassthroughCopy("root/img");
  eleventyConfig.addPassthroughCopy("root/css");
  eleventyConfig.addPassthroughCopy("root/docs");
  eleventyConfig.addPassthroughCopy("root/favicon.ico");
  // The following line will pass through all the markdown files so am not doing that
  // eleventyConfig.addPassthroughCopy({"root": "/"});
  // Because all my files expect the /img/ folder to be at the top level
  // eleventyConfig.addPassthroughCopy({"root/img": "/img"});
  // eleventyConfig.addPassthroughCopy({"root/docs": "/"});

  return {
    dir: {
	  input: "root",
      output: "./_site", // Equivalent to Jekyll's destination property
      includes: "_includes",
      layouts: "_layouts",
    },
  };
};
