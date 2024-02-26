module.exports = {
    "env": {
        "node": true,
        "es6": true
    }
    rules: {
        "jest/expect-expect": "off",
        "jest/prefer-expect-assertions": "off",
        "jest/valid-expect": "off"
    },
    extends: [
        // Other extends...
        "plugin:jest/recommended"
    ],
}
