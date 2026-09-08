# Changelog

## [0.3.2](https://github.com/ytihianine/grist-doc-to-dbml/compare/v0.3.1...v0.3.2) (2026-09-08)


### Others

* **deps:** update dependency numpy to v2.5.3 ([#23](https://github.com/ytihianine/grist-doc-to-dbml/issues/23)) ([c76aaea](https://github.com/ytihianine/grist-doc-to-dbml/commit/c76aaeaf2abdae54d4be22c93b460237dbc8424f))

## [0.3.1](https://github.com/ytihianine/grist-doc-to-dbml/compare/v0.3.0...v0.3.1) (2026-08-19)


### Others

* **deps:** update dependency numpy to v2.5.2 ([#21](https://github.com/ytihianine/grist-doc-to-dbml/issues/21)) ([6f70c66](https://github.com/ytihianine/grist-doc-to-dbml/commit/6f70c66481934a7ea2acc63e95b99838bc9bc6b4))
* **deps:** update dependency pre-commit to v4.6.2 ([#22](https://github.com/ytihianine/grist-doc-to-dbml/issues/22)) ([e9654f7](https://github.com/ytihianine/grist-doc-to-dbml/commit/e9654f7067d8bce1015fe1357c426f0818aa0a74))
* **docs:** rename repo ([ceb90df](https://github.com/ytihianine/grist-doc-to-dbml/commit/ceb90df6007953e7532f002cd520ca798b7d4dbf))

## [0.3.0](https://github.com/ytihianine/grist-doc-to-db-parser/compare/v0.2.0...v0.3.0) (2026-08-05)


### Features

* **src:** simplify type conversion and add step logs ([609c077](https://github.com/ytihianine/grist-doc-to-db-parser/commit/609c077956c50a92d832ad7d3794c118dc2f58f3))


### Bug Fixes

* **src:** update Ref and Reflist type conversion ([6f75d09](https://github.com/ytihianine/grist-doc-to-db-parser/commit/6f75d0965eb4b35274d5b308d2efa4da4de9253a))


### Others

* **img:** update ERD image ([eef2760](https://github.com/ytihianine/grist-doc-to-db-parser/commit/eef276083c8c3611f25b8da0cdb3acb80841df37))

## [0.2.0](https://github.com/ytihianine/grist-doc-to-db-parser/compare/v0.1.1...v0.2.0) (2026-08-05)


### Features

* **main:** update main to use new functions ([8bbcb15](https://github.com/ytihianine/grist-doc-to-db-parser/commit/8bbcb158d88596dd7383a66118eaafb32d293ddc))
* **src:** add logger to print information in console ([38a0dbd](https://github.com/ytihianine/grist-doc-to-db-parser/commit/38a0dbde908d62230c242b4d60f5083f7da44b8b))
* **src:** convert str output path to Path object ([099d835](https://github.com/ytihianine/grist-doc-to-db-parser/commit/099d83507e1707ef4591157e1e0b82d2aadbaa8f))
* **src:** refactor and simplify processing functions ([840a233](https://github.com/ytihianine/grist-doc-to-db-parser/commit/840a2338f28f3d405f08e5edefd8b15eaca7b331))


### Bug Fixes

* **src:** replace all hardcoded column name values by config attributs ([9dabb93](https://github.com/ytihianine/grist-doc-to-db-parser/commit/9dabb93369746e960544b3bb64e4fae579aa54d2))


### Documentations

* update project documentation and add images to illustrate the purpose of the script ([c67e938](https://github.com/ytihianine/grist-doc-to-db-parser/commit/c67e93806d8b640a36cc4963d8cf969e57823f00))


### Others

* add dbml files to gitignore ([d02fefe](https://github.com/ytihianine/grist-doc-to-db-parser/commit/d02fefe21243c66f69039757e5d206862abd79f3))
* **src:** add step logs ([e8fd2d6](https://github.com/ytihianine/grist-doc-to-db-parser/commit/e8fd2d619b172da95aa937acee50fb938bcbd0be))

## [0.1.1](https://github.com/ytihianine/grist-doc-to-db-parser/compare/v0.1.0...v0.1.1) (2026-08-05)


### Bug Fixes

* **ci:** update precommit config file name ([cbf366d](https://github.com/ytihianine/grist-doc-to-db-parser/commit/cbf366de3c4d5808bf78335eedcaaaab4ec7ef0e))


### Others

* **ci:** add pre-commit-config ([a5f7640](https://github.com/ytihianine/grist-doc-to-db-parser/commit/a5f7640d69f3c64d36a69c29c2baacb623106190))
* **ci:** add python linting workflow ([992357d](https://github.com/ytihianine/grist-doc-to-db-parser/commit/992357d335eda3a426266e09505a00f1e7358aec))
* **ci:** rename precommit config file ([214697c](https://github.com/ytihianine/grist-doc-to-db-parser/commit/214697cfae77596aa9008bd80a6eb21eedd7939c))
* **ci:** replace requirements with pyproject ([b365b65](https://github.com/ytihianine/grist-doc-to-db-parser/commit/b365b6547bbf64c249b5d5b0b6a5e2d6cc2c498d))
* **precommit:** exclude md files from end-of-file-fixer hook ([252d763](https://github.com/ytihianine/grist-doc-to-db-parser/commit/252d76317005c24b2cdc53f1edeb43666250c092))
* **precommit:** exclude md files from trailing-whitespace hook ([95c42ad](https://github.com/ytihianine/grist-doc-to-db-parser/commit/95c42adb90b6d08dfc534f5ea8ed8d4a9cd747ee))
* update gitignore ([eb7e298](https://github.com/ytihianine/grist-doc-to-db-parser/commit/eb7e298536a7df2a5531f023beb96a2b0aedc8dc))

## 0.1.0 (2026-08-05)


### Features

* add scripts to parse a grist doc into a dblm file ([5dbdb38](https://github.com/ytihianine/grist-doc-to-db-parser/commit/5dbdb38de48184a041a636d94c7ac98ac13157ba))
* allow the user to lowercase colnames and/or tbl names ([ec911c4](https://github.com/ytihianine/grist-doc-to-db-parser/commit/ec911c4e531745d98b544300a0a63f9c8b8e551b))
* allow to export df to csv before generating dbml file ([59887b6](https://github.com/ytihianine/grist-doc-to-db-parser/commit/59887b6105c4ecabac2a58997e2a655ccabd8b51))


### Bug Fixes

* **parser:** add id_ prefix to reference columns ([333f330](https://github.com/ytihianine/grist-doc-to-db-parser/commit/333f330f5dd7bf814f2e0c9c24fd2d530720afe7))


### Documentations

* add readme ([80df85a](https://github.com/ytihianine/grist-doc-to-db-parser/commit/80df85a737d86fa7a69bcaa8d734322e176b6e49))
* specify file name ([66947d7](https://github.com/ytihianine/grist-doc-to-db-parser/commit/66947d7ebeb5e0d9ab55d79f22d1182a58730121))


### Others

* add gitignore file ([a03934d](https://github.com/ytihianine/grist-doc-to-db-parser/commit/a03934d926412cacaee52f3518b8d69157ac5f2a))
* **ci:** add release please workflow ([621267e](https://github.com/ytihianine/grist-doc-to-db-parser/commit/621267e8934fd4513201bce5474a14666aa7f589))
* **ci:** add release-please config files ([79e639a](https://github.com/ytihianine/grist-doc-to-db-parser/commit/79e639a9581e8958c811d6f577f394fd87c23166))
* Configure Renovate ([c8a4508](https://github.com/ytihianine/grist-doc-to-db-parser/commit/c8a4508a16ab8672624ff37ffe50cb9f1a99d520))
* **deps:** update dependency numpy to v2.5.0 ([1344738](https://github.com/ytihianine/grist-doc-to-db-parser/commit/1344738715304b0a21f944abcef5bb9fbfe69df8))
* **deps:** update dependency numpy to v2.5.0 ([38f6daf](https://github.com/ytihianine/grist-doc-to-db-parser/commit/38f6daf5e791a0ae64969bf932d18ef389f14cbf))
* **deps:** update dependency numpy to v2.5.1 ([5472342](https://github.com/ytihianine/grist-doc-to-db-parser/commit/54723421b0e783382f9fea136735180cbe0e1bf4))
* **deps:** update dependency numpy to v2.5.1 ([a166df2](https://github.com/ytihianine/grist-doc-to-db-parser/commit/a166df28159d223a3a0c0b2746569d30b5086416))
* **deps:** update dependency pandas to v2.3.3 ([b8d316f](https://github.com/ytihianine/grist-doc-to-db-parser/commit/b8d316f726ceec72f20cba3f44fc8815dad85859))
* **deps:** update dependency pandas to v2.3.3 ([31ab788](https://github.com/ytihianine/grist-doc-to-db-parser/commit/31ab788c17fc1daa1f6e195844c8a1ee7e1b0643))
* **deps:** update dependency pandas to v2.3.3 ([6ba29be](https://github.com/ytihianine/grist-doc-to-db-parser/commit/6ba29be91dffdd2dfa91e96489b4b1fa3cc0a531))
* **deps:** update dependency pandas to v2.3.3 ([cc69dde](https://github.com/ytihianine/grist-doc-to-db-parser/commit/cc69dde7f89c5df3f6a64050229e1045f18fe86b))
* **deps:** update dependency pandas to v2.3.3 ([6dd9487](https://github.com/ytihianine/grist-doc-to-db-parser/commit/6dd9487e8df09d1959cecc245287bb555fb18dd8))
* **deps:** update dependency pandas to v2.3.3 ([3caf5d0](https://github.com/ytihianine/grist-doc-to-db-parser/commit/3caf5d03363bab39682e31a97d16540003a2880e))
* **deps:** update dependency pandas to v3 ([66a0833](https://github.com/ytihianine/grist-doc-to-db-parser/commit/66a0833d3d0823cfc4f2446bf5efef67ecf77d78))
* **deps:** update dependency pandas to v3 ([fed3862](https://github.com/ytihianine/grist-doc-to-db-parser/commit/fed38626c00ec646e3ff765347d50efb5bdb0e67))
* **deps:** update dependency pandas to v3.0.5 ([#15](https://github.com/ytihianine/grist-doc-to-db-parser/issues/15)) ([8ef678e](https://github.com/ytihianine/grist-doc-to-db-parser/commit/8ef678ee2f0df7bb607f70aef1dfb799083dcb1a))
* ignore csv file ([b453167](https://github.com/ytihianine/grist-doc-to-db-parser/commit/b45316742b95e559f975c3dbcdf68046ab662d8a))
* update gitignore ([2317062](https://github.com/ytihianine/grist-doc-to-db-parser/commit/23170622379b22a5ab6329a64c86241ffba7eed2))
