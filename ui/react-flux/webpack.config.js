const path = require('path');

module.exports = {
    entry: path.resolve(__dirname, './src/index.js'),
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader'],
            },
            {
                test: /\.css$/,
                exclude: /node_modules/,
                use: ['style-loader', 'css-loader'],
            }
        ],
    },
    resolve: {
        extensions: ['*', '.js', '.jsx'],
    },
    output: {
        path: path.resolve(__dirname, '../static/js'),
        filename: 'bundle.js',
    },
    devServer: {
        contentBase: path.resolve(__dirname, './public'),
    },
    watch: true,
    watchOptions: {
        ignored: '**/node_modules',
        aggregateTimeout: 200,
        poll: 1000,
    },
};