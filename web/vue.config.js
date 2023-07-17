const { defineConfig } = require('@vue/cli-service');
module.exports = {
  outputDir: '../static',
  indexPath: '../templates/index.html',
  assetsDir: 'static/',
  configureWebpack: {
    resolve: {
      alias: {},
    },
  },
};
