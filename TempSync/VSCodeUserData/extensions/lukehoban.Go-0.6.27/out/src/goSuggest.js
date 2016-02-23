/*---------------------------------------------------------
 * Copyright (C) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------*/
'use strict';
var vscode = require('vscode');
var cp = require('child_process');
var path_1 = require('path');
var goPath_1 = require('./goPath');
var util_1 = require('./util');
function vscodeKindFromGoCodeClass(kind) {
    switch (kind) {
        case 'const':
        case 'package':
        case 'type':
            return vscode.CompletionItemKind.Keyword;
        case 'func':
            return vscode.CompletionItemKind.Function;
        case 'var':
            return vscode.CompletionItemKind.Field;
    }
    return vscode.CompletionItemKind.Property; // TODO@EG additional mappings needed?
}
var GoCompletionItemProvider = (function () {
    function GoCompletionItemProvider() {
        this.gocodeConfigurationComplete = false;
        this.recursion = false;
        this.defaultSuggestions = [];
    }

    GoCompletionItemProvider.prototype.provideCompletionItems2 = function(document, position, token) {
        var self = this;
        console.log('call provideCompletionItems', this.defaultSuggestions);

        return [];

        if (self.recursion) {
            console.log('return defaultSuggestions');
            return self.defaultSuggestions;
        }

        self.recursion = true;

        var _provideCompletionItems = GoCompletionItemProvider.prototype.provideCompletionItems;
        delete GoCompletionItemProvider.prototype.provideCompletionItems;

        return new Promise(function (resolve, reject) {
            vscode.commands.executeCommand('vscode.executeCompletionItemProvider', document.uri, position).then(function (suggestions) {
                // console.log('command done');
                // self.recursion = false;
                // resolve([]);
            });
        })

        // if (self.recursion) {
        //     console.log('return defaultSuggestions');
        //     return self.defaultSuggestions;
        // }

        self.recursion = true;

        return new Promise(function (resolve, reject) {
            vscode.commands.executeCommand('vscode.executeCompletionItemProvider', document.uri, position).then(function (suggestions) {
                console.log('command done');
                self.recursion = false;
                resolve([]);
            });
        })
    }

    GoCompletionItemProvider.prototype.provideCompletionItems = function (document, position, token) {
        // return this.provideCompletionItems2(document, position, token);

        return this.ensureGoCodeConfigured().then(function () {

            return new Promise(function (resolve, reject) {
                var filename = document.fileName;
                if (document.lineAt(position.line).text.match(/^\s*\/\//)) {
                    return resolve([]);
                }
                // get current word
                var wordAtPosition = document.getWordRangeAtPosition(position);
                var currentWord = '';
                if (wordAtPosition && wordAtPosition.start.character < position.character) {
                    var word = document.getText(wordAtPosition);
                    currentWord = word.substr(0, position.character - wordAtPosition.start.character);
                }
                if (currentWord.match(/^\d+$/)) {
                    return resolve([]);
                }
                var offset = document.offsetAt(position);
                var gocode = goPath_1.getBinPath('gocode');
                // Unset GOOS and GOARCH for the `gocode` process to ensure that GOHOSTOS and GOHOSTARCH
                // are used as the target operating system and architecture. `gocode` is unable to provide
                // autocompletion when the Go environment is configured for cross compilation.
                var env = Object.assign({}, process.env, { GOOS: '', GOARCH: '' });
                // Spawn `gocode` process
                var p = cp.execFile(gocode, ['-f=json', 'autocomplete', filename, 'c' + offset], { env: env }, function (err, stdout, stderr) {
                    try {
                        if (err && err.code === 'ENOENT') {
                            vscode.window.showInformationMessage('The "gocode" command is not available.  Use "go get -u github.com/nsf/gocode" to install.');
                        }
                        if (err)
                            return reject(err);
                        var results = JSON.parse(stdout.toString());
                        if (!results[1]) {
                            // 'Smart Snippet' for package clause
                            // TODO: Factor this out into a general mechanism
                            if (!document.getText().match(/package\s+(\w+)/)) {
                                var defaultPackageName = path_1.basename(document.fileName) === 'main.go'
                                    ? 'main'
                                    : path_1.basename(path_1.dirname(document.fileName));
                                var packageItem = new vscode.CompletionItem('package ' + defaultPackageName);
                                packageItem.kind = vscode.CompletionItemKind.Snippet;
                                packageItem.insertText = 'package ' + defaultPackageName + '\r\n\r\n';
                                return resolve([packageItem]);
                            }
                            return resolve([]);
                        }
                        var suggestions = results[1].map(function (suggest) {
                            var item = new vscode.CompletionItem(suggest.name);
                            item.kind = vscodeKindFromGoCodeClass(suggest.class);
                            item.detail = suggest.type;
                            var conf = vscode.workspace.getConfiguration('go');
                            if (conf.get('useCodeSnippetsOnFunctionSuggest') && suggest.class === 'func') {
                                var params = util_1.parameters(suggest.type.substring(4));
                                var paramSnippets = [];
                                for (var i in params) {
                                    var param = params[i].trim();
                                    if (param) {
                                        param = param.replace('{', '\\{').replace('}', '\\}');
                                        paramSnippets.push('{{' + param + '}}');
                                    }
                                }
                                item.insertText = suggest.name + '(' + paramSnippets.join(', ') + '){{}}';
                            }
                            return item;
                        });
                        resolve(suggestions);
                    }
                    catch (e) {
                        reject(e);
                    }
                });
                p.stdin.end(document.getText());
            });
        });
    };
    GoCompletionItemProvider.prototype.ensureGoCodeConfigured = function () {
        var _this = this;
        return new Promise(function (resolve, reject) {
            if (_this.gocodeConfigurationComplete) {
                return resolve();
            }
            var gocode = goPath_1.getBinPath('gocode');
            cp.execFile(gocode, ['set', 'propose-builtins', 'true'], {}, function (err, stdout, stderr) {
                cp.execFile(gocode, ['set', 'autobuild', 'true'], {}, function (err, stdout, stderr) {
                    resolve();
                });
            });
        });
    };
    return GoCompletionItemProvider;
})();
exports.GoCompletionItemProvider = GoCompletionItemProvider;
//# sourceMappingURL=goSuggest.js.map