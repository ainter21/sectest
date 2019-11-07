# Google Gruyere

ID: 610613689515103742845857127100735463027

## XSS

Combinations for <> code check:


* %3e%3c
* %253e%253c
* %c0%be%c0%bc
* %26gt;%26lt;
* %26amp;gt;%26amp;lt;
* \074\x3c\u003c\x3C\u003C\X3C\U003C
* +ADw-+AD4-

Sometimes the sanitizing functions are incomplete, so you can try for some allowed **tags** or **attributes**.

HTML permits some bad tag syntax. It can be used to perform some attacks.

It is always better to create whitlesists than blacklist. Attributes like `href`, `src` and `style` are dangerous because they can be used to inject Javascript.

You always need to look for library documentation, and how function are implementes. Single or double quotes in HTML attributes, for example, are not always treated at the same way.

**onload**: this attribute is supposed to be in `body` or in `frameset` tag by some browser, but not the browsers! 

Some browsers allow you to include script in the stylsheets (i.e. Internet Explorer).

