const Discord = require("discord.js");
const client = new Discord.Client();
const prefix = '!';

client.on("message", async message => {
  if (message.content.startsWith(prefix)) {
    const args = message.content.slice(prefix.length).split(" ");
    const command = args.shift().toLowerCase();

    if (command === "ping") {
        message.reply("pong");
    }
  }
});

client.login("token");