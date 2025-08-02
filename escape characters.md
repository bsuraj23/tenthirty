\n - Newline
Moves the text to the next line.

Example: "Hello\nWorld" →

\t - Tab
Adds a horizontal tab space.

Example: "A\tB" → A B

\\ - Backslash
Prints a single backslash.

Example: "C:\\Users" → C:\Users

\' - Single Quote
Allows you to use a single quote inside single-quoted strings.

Example: 'It\'s OK' → It's OK

\" - Double Quote
Allows you to use double quotes inside double-quoted strings.

Example: "She said: \"Hi\"" → She said: "Hi"

\r - Carriage Return
Moves the cursor to the beginning of the line.

Example: "123\rAB" → AB3

\b - Backspace
Removes the character before it.

Example: "Hel\blo" → Helo

\f - Form Feed
Advances to the next page (rarely used).

Example: "Line1\fLine2" → Line1▯Line2 (effect depends on editor)

\a - Bell/Alert
Triggers a beep sound (if supported).

Example: print("\a") → 🔔

\N{name} - Named Unicode character
Uses a Unicode character name.

Example: "\N{copyright sign}" → ©
