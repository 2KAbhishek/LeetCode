/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, newColor) {
    let R = image.length;
    let C = image[0].length;
    let oldColor = image[sr][sc];

    if (oldColor == newColor) return image;

    var dfs = function(r, c) {
        if (image[r][c] == oldColor){
            image[r][c] = newColor;
            if (r >= 1) dfs(r-1, c);
            if (r + 1 < R) dfs(r+1, c);
            if (c >= 1) dfs(r, c-1);
            if (c + 1 < C) dfs(r, c+1);
        }
    }

    dfs(sr,sc);
    return image;
};

