# ❌ No-as-a-Service

<p align="center">
  <img src="assets/imgs/naas-with-no-logo-bunny.png" width="800" alt="No-as-a-Service Banner" width="70%"/>
</p>


Ever needed a graceful way to say “no”?  
This tiny API returns random, generic, creative, and sometimes hilarious rejection reasons — perfectly suited for any scenario: personal, professional, student life, dev life, or just because.

Built for humans, excuses, and humor.

This is a [FastAPI](https://fastapi.tiangolo.com/) port of the original Node/Express [no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) by hotheadhacker.

## 🚀 API Usage

**Base URL**
```
https://naas-be7b797c.fastapicloud.dev/no
```

**Method:** `GET`  
**Rate Limit:** `120 requests per minute per IP`

### 🔄 Example Request
```http
GET /no
```

### ✅ Example Response
```json
{
  "reason": "This feels like something Future Me would yell at Present Me for agreeing to."
}
```

Use it in apps, bots, landing pages, Slack integrations, rejection letters, or wherever you need a polite (or witty) no.

---

## 🛠️ Self-Hosting

Want to run it yourself? It’s lightweight and simple. You need [uv](https://docs.astral.sh/uv/); it installs Python 3.14 for you if needed.

### 1. Clone this repository
```bash
git clone https://github.com/bashu/no-as-a-service-fastapi.git
cd no-as-a-service-fastapi
```

### 2. Install dependencies
```bash
uv sync
```

### 3. Start the server
```bash
uv run fastapi run
```

The API will be live at:
```
http://localhost:8000/no
```

Interactive API docs are at `http://localhost:8000/docs`.

For development with auto-reload, use `uv run fastapi dev` instead.

You can also change the port using an environment variable:
```bash
PORT=5000 uv run fastapi run
```

### 🐳 Docker
```bash
docker build -t naas-fastapi .
docker run --rm -p 8000:8000 naas-fastapi
```

---

## 📁 Project Structure

```
no-as-a-service-fastapi/
├── main.py             # FastAPI app
├── reasons.json        # 1000+ universal rejection reasons
├── pyproject.toml      # dependencies (managed with uv)
├── uv.lock
├── Dockerfile
├── .devcontainer.json  # VS Code / Github devcontainer setup
└── README.md
```

---

## ⚓ Devcontainer

If you open this repo in Github Codespaces, it will automatically use `.devcontainer.json` to set up your environment.  If you open it in VSCode, it will ask you if you want to reopen it in a container.

---
## Projects Using No-as-a-Service

Here are some projects and websites that creatively integrate [no-as-a-service](https://naas.isalman.dev/no) to deliver humorous or programmatic "no" responses:

1. **[no-as-a-service-rust](https://github.com/ZAZPRO/no-as-a-service-rust)**  
   Rust implementation of this project.

2. **[CSG Admins](https://csg-admins.de)**  
   A system administration and gaming service hub using no-as-a-service to provide playful negative responses across some admin panels and commands.

3. **[FunnyAnswers - /no endpoint](https://www.funnyanswers.lol/no)**  
   A humor-focused API playground that includes a mirror or wrapper for no-as-a-service, perfect for developers exploring fun HTTP-based responses.

4. **[Gerador de Frases Aleatórias (pt-BR)](https://github.com/timeuz/frases-aleatorias)**
   Uma reinterpretação em Python com frases em português, frontend e novas categorias.

5. **[NoAsAnApp](https://github.com/omar-jarid/NoAsAnApp)**  
   A simple native Android app calling no-as-a-service to provide negative responses.

6. **[FunnyReasons](https://github.com/amitbiswal007/FunnyReasons)**  
   A simple Web app using `no-as-a-service` to provide funny reasons to say No.

7. **[How About No?](https://github.com/lloyd094/How-About-No-)**
   A basic GUI using no-as-a-service as the backend. Built with docker in mind.
   
8. **[no-as-a-service-asp](https://github.com/sapph42/no-as-a-service)**  
   A straight-forward implementation of NaaS in ASP.NET Core
   
9. **[No as a Service - Raycast Extension](https://www.raycast.com/nedini/no-as-a-service)**  
   Get a random No from within Raycast. Just install the extension from the Raycast store, open Raycast, then type in 'Random No'. Raycast extension: [No as a Service](https://www.raycast.com/nedini/no-as-a-service).
10. **[Nopeify]([https://github.com/omar-jarid/NoAsAnApp](https://apps.apple.com/us/app/nopeify/id6757724453))**  
   A simple native iOS app calling no-as-a-service to provide negative responses.

11. **[No-as-a-Service - Slack App](https://github.com/pro100svitlo/no-as-a-service-slack-app)**  
   Get a random `No` from within Slack. [Install](https://slack.com/oauth/v2/authorize?client_id=2550998207090.10222067205218&scope=commands,chat:write&user_scope=) the app to your workspace and then use the `/no` command to get a random response. 

12. **[No-as-a-Service - Signal Bot](https://github.com/samtate/signal-no-as-a-service-bot)**  
    Get a random `No` from within Signal. Deploy the Docker container, link your Signal account, and use the `/no` command to get a random response.

13. **[No-as-a-Service GNOME Search](https://extensions.gnome.org/extension/9186/naas-gnome-search/)**
   GNOME search provider for the No-as-a-Service API. Type 'no' to get a random excuse. Click or press Enter to copy to clipboard.

14. **[Nope App](https://github.com/foss-nope/apple-nope) for iPhone and iPad. Available on [AppStore](https://apps.apple.com/app/id6759522055) **  
    Simple OpenSource iOS app inspired by this service to find and curate reasons to say no!

15. **[No MCP](https://github.com/clafoutis42/no-mcp)**  
    Perfect for when you want your AI to be consistently negative or just want to add some humor to your MCP setup.

16. **[Your Project Here?](https://github.com/YOUR_REPO)**
   If you're using no-as-a-service in your project, open a pull request to be featured here!

---

> Want to use no-as-a-service in your own project? Check out the usage section in this README and start returning **"no"** like a pro.
---

## 👤 Author

Created with creative stubbornness by [hotheadhacker](https://github.com/hotheadhacker)

FastAPI port by [bashu](https://github.com/bashu)

---

## 📄 License

MIT — do whatever, just don’t say yes when you should say no.

---

## 🐧 Testimonials

> "I tried to integrate No-as-a-Service into the Linux kernel to reject bad patches automatically, but it started rejecting my own commits. 10/10, absolutely ruthless."
> 
> — **Linus Torvalds** (probably)
