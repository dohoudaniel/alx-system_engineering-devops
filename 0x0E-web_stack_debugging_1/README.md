## 0x0D-web_stack_debugging_0

In this ALX SE project, I learn how to debug web stacks on Docker conatiners and images.

The concepts I learned in this project are:
- Docker containers
- Docker Images
- Commands used to debug web connections:
	- netstat
	- w
	- history
	- top
	- df
	- free
	- htop
	- ifconfig
	- telnet
	- iptables
	- ufw
	- pgrep
	- ps auxf

In this project, I debugged an Nginx server.

---
## Explanation of the command
`sed -i 's/8080/80/g' /etc/nginx/sites-enabled/default`

The `sed` command you provided is a command-line tool used for text manipulation, particularly for finding and replacing text within files. Let's break down the command:

- `sed`: This is the command itself, which stands for "stream editor." It's used for filtering and transforming text.

- `-i`: This option tells `sed` to perform the operation "in place," meaning it will directly modify the contents of the specified file instead of writing the output to the terminal or a new file.

- `'s/8080/80/g'`: This is the substitution command for `sed`. It consists of the following components:
  - `s`: This is the substitution command in `sed`.
  - `/8080/`: This is the pattern to be replaced. In this case, it's searching for the string "8080."
  - `/80/`: This is the replacement text. It will replace occurrences of "8080" with "80."
  - `g`: This modifier stands for "global" and tells `sed` to replace all occurrences of the pattern, not just the first one found in each line.

- `/etc/nginx/sites-enabled/default`: This is the path to the file where the substitution operation will be performed. In this case, it's the Nginx configuration file located at `/etc/nginx/sites-enabled/default`.

So, in summary, the command `sed -i 's/8080/80/g' /etc/nginx/sites-enabled/default` searches through the Nginx configuration file `/etc/nginx/sites-enabled/default` and replaces all occurrences of "8080" with "80" in place, meaning the changes are directly applied to the file. This is commonly used to update port configurations in Nginx files, as in this case, changing the port from 8080 to 80.

#### Debugging is Fun 🥂
