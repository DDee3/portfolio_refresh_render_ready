import os

from flask import Flask, jsonify, render_template

app = Flask(__name__)
# Cache static assets (CSS, images) in browsers for 7 days
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 604800

PROJECTS = [
    {
        "name": "Market Oracle — AI Stock Predictor",
        "tech": "Python · Machine Learning · APIs · Data Analysis",
        "description": (
            "Backend-focused stock market prediction project combining machine-learning models, "
            "external market data, and a custom Stock Almanac dataset to compare historical "
            "patterns with current predictions."
        ),
        "link": "https://huggingface.co/spaces/CallmeDdee/Market-Orcale",
        "cta": "View live project",
        "status": None,
    },
    {
        "name": "ĒLAN",
        "tech": "Flask · E-commerce · UI/UX",
        "description": (
            "A modern fashion e-commerce web application designed around a clean, premium shopping experience. "
            "ĒLAN features a responsive storefront, product browsing, cart functionality, user authentication, "
            "and a polished luxury-inspired interface built for both desktop and mobile."
        ),
        "link": "https://luxe-clothing-store-xq9e.onrender.com/",
        "cta": "View Live Site",
        "status": "Live project",
},
    {
        "name": "KitchenHub",
        "tech": "UI/UX · Product Concept",
        "description": (
            "A cooking-app concept developed through interface exploration, layout guidelines, "
            "and structured pitch materials."
        ),
        "link": "https://kitchenhub-flask.onrender.com",
        "cta": "View Live Project",
        "status": "Concept project",
    },
    {
        "name": "AI Career Decision Engine",
        "tech": "Storyboard · Framework Design",
        "description": (
            "A visual decision framework that maps common career problems to practical, "
            "AI-assisted paths for research, comparison, and next-step planning."
        ),
        "link": None,
        "cta": None,
        "status": "Framework concept",
    },
    {
        "name": "Personal Developer Portfolio",
        "tech": "Python · Flask · HTML · CSS",
        "description": (
            "This responsive portfolio, built as a lightweight Flask application with a "
            "minimal interface and production deployment configuration for Render."
        ),
        "link": None,
        "cta": None,
        "status": "Current portfolio",
    },
]

BIO = (
    "I build practical web experiences with Python and modern AI-assisted development workflows. "
    "My background also includes high-pressure hospitality, telecommunications support at Singtel, "
    "and retail sales, which shaped how I communicate with customers, understand real-world needs, "
    "and stay effective when problems need to be solved quickly."
)

LANGUAGES = [
    "English",
    "Chinese — Simplified",
    "Burmese",
]


@app.get("/")
def home():
    return render_template(
        "index.html",
        projects=PROJECTS,
        bio=BIO,
        languages=LANGUAGES,
    )


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


@app.after_request
def set_headers(response):
    """Add baseline security headers and long-lived caching for static assets."""
    response.headers.setdefault(
        "Content-Security-Policy",
        "default-src 'self'; img-src 'self' data:; style-src 'self'; "
        "frame-ancestors 'none'; base-uri 'self'; form-action 'self'",
    )
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("X-Frame-Options", "DENY")
    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    debug = os.environ.get("FLASK_DEBUG") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
