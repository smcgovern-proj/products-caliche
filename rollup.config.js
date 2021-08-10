import typescript from '@rollup/plugin-typescript';

export default {
  input: 'src/',
  output: {
    dir: 'build',
    format: 'cjs'
  },
  plugins: [typescript()]
};
