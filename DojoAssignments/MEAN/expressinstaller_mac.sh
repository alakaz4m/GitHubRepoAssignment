echo -e 'calling npm init -y'
cmd="npm init -y"
$cmd
echo -e 'echo installing express, body-parser, ejs, express-session, and dependencies..'
npm install express ejs body-parser express-session