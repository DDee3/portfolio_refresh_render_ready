# Nay Thar Htet — Portfolio

A lightweight Flask portfolio prepared for deployment on Render.

## What changed

- Reworked the visual design into a cleaner, more editorial portfolio layout.
- Removed the Skills block/tags while keeping the Languages section.
- Added responsive navigation and mobile layouts.
- Optimized the large profile PNG into a much smaller WebP image for faster loading.
- Added clearer project presentation and calls to action.
- Replaced placeholder social links with a direct email contact instead of publishing fake URLs.
- Added accessible navigation, focus behavior, reduced-motion support, and metadata.
- Reduced `requirements.txt` to only the packages this app needs.
- Added a `/health` route and root-level `render.yaml` for Render Blueprint deployment.

## Run locally

```bash
python -m venv .venv
```

Activate the environment, then:

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Deploy on Render with a Blueprint

1. Upload the **contents of this folder** to the root of a GitHub repository.
2. Confirm `render.yaml`, `app.py`, and `requirements.txt` are visible on the repository's main page.
3. In Render, choose **New → Blueprint**.
4. Select the repository and keep the Blueprint path as `render.yaml`.
5. Apply the Blueprint.

Render will install dependencies with `pip install -r requirements.txt` and start the app with `gunicorn app:app`.

## Personal links

The previous GitHub and LinkedIn links were placeholders (`yourusername`), so they were removed. Add your real URLs to the footer when you are ready.
