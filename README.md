# Kitty migration notes

This config was generated from your iTerm2 `Default` profile.

Carried over:

- Monaco 15 pt font
- Catppuccin Mocha colors from iTerm2
- 80x25 startup window
- 1000 lines of scrollback
- beam cursor
- visual bell, audio bell disabled
- no transparency
- zsh login shell
- common macOS/iTerm tab, clipboard, fullscreen, clear, split, and font-size shortcuts
- Option-left/right and Option-delete word navigation/deletion

Left in your existing dotfiles:

- oh-my-zsh
- starship
- aliases/functions
- vim runtime and `.vimrc`

Kitty launches `/bin/zsh -l`, so those should load the same way they do in iTerm2.

Try it with:

```sh
kitty --config ~/.config/kitty/kitty.conf
```

If Kitty is not installed yet:

```sh
brew install --cask kitty
```

