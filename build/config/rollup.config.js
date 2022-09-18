'use strict'

const { babel } = require('@rollup/plugin-babel')

const pkg = require('../../package')
const year = new Date().getFullYear()
const banner = `/*!
 * hsiams v${pkg.version} (${pkg.homepage})
 * Copyright 2014-${year} ${pkg.author}
 * Licensed under MIT (https://github.com/ColorlibHQ/hsiams/blob/master/LICENSE)
 */`

module.exports = {
  input: 'build/js/hsiams.js',
  output: {
    banner,
    file: 'dist/js/hsiams.js',
    format: 'umd',
    globals: {
      jquery: 'jQuery'
    },
    name: 'hsiams'
  },
  external: ['jquery'],
  plugins: [
    babel({
      exclude: 'node_modules/**',
      // Include the helpers in the bundle, at most one copy of each
      babelHelpers: 'bundled'
    })
  ]
}
