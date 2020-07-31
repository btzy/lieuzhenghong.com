const markdownIt = require("markdown-it");
const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");

module.exports = function (eleventyConfig) {
  const md = new markdownIt({
    html: true,
  });

  eleventyConfig.addPairedShortcode("markdown", (content) => {
    return md.render(content);
  });

  // add syntax highlighting plugin
  // https://www.11ty.dev/docs/plugins/syntaxhighlight/
  eleventyConfig.addPlugin(syntaxHighlight);

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

  eleventyConfig.addPassthroughCopy("img");
  eleventyConfig.addPassthroughCopy("css");

  return {
    dir: {
      output: "./_site", // Equivalent to Jekyll's destination property
      includes: "_includes",
      layouts: "_layouts",
    },
  };
};
