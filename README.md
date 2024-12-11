# MOSHPIT

## Enabling tab completion

### Bash

To enable tab completion in Bash, run the following command or add it to your
`.bashrc`/`.bash_profile`:

```bash
source tab-mosh
```

### ZSH

To enable tab completion in ZSH, run the following commands or add them to your
`.zshrc`:

```bash
autoload -Uz compinit && compinit && autoload bashcompinit && bashcompinit && source tab-mosh
```
