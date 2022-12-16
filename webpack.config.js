const MiniCssExtractPlugin = require("mini-css-extract-plugin");

const path = require("path");
module.exports = {
  mode: "production",
  entry: "./src/static/js/main.js",
  output: {
    path: path.resolve(__dirname, "src/static/dist"),
    filename: "main.js",
  },
  module: {
    rules: [
      {
        test: /\.js$/i,
        include: path.resolve(__dirname, "js"),
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
        },
      },
      {
        test: /\.css$/,
        exclude: /node_modules/,
        use: [
          MiniCssExtractPlugin.loader,
          { loader: "css-loader", options: { url: false } },
          "postcss-loader",
        ],
      },
    ],
  },
  devServer: {
    static: "src/static/dist",
    watchContentBase: true,
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "main.css",
    }),
  ],
};
