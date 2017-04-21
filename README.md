# maybetyped

Checks the DefinitelyTyped repo to see if an npm module has typings.

## Usage

```bash
$ ./maybetyped.py classnames
YES
classnames is typed
https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/classnames
```

```bash
$ POTENTIAL_MODULE="classnames"
$ ./maybetyped.py $POTENTIAL_MODULE && yarn add $POTENTIAL_MODULE && yarn add --dev @types/$POTENTIAL_MODULE
```
