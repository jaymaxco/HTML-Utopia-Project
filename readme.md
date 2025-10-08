# HTML Utopia Project

A demonstration / starter template for a fully fluid, responsive site built using the **Utopia** design system — no media queries required.

---

## 🔍 Overview

This project showcases a CSS-only approach to a modern, responsive layout system using the [Utopia fluid typography and spacing method](https://utopia.fyi/).  
It includes automatic theme detection (light/dark mode), an image carousel, and subtle animations — all without JavaScript.

### Key Goals

- Fully responsive design with **no media queries**
- Fluid scaling for typography, spacing, and layout grid
- **Automatic light/dark mode** detection
- **Pure CSS image carousel** and animations
- **CSS custom properties** for modular, themeable design

---

## ✨ Features

- **Responsive without breakpoints** — all scaling is handled with `clamp()` values.  
- **Utopia system integration** — values generated from [utopia.fyi/type/calculator](https://utopia.fyi/type/calculator).  
- **Automatic theme detection** — uses `prefers-color-scheme`.  
- **CSS-only image carousel** — leverages animation and keyframes.  
- **Variable-driven design system** — edit colors, type, and layout globally with CSS variables.  
- **Component-based structure** — styles and tokens are modular and easy to extend.

---

## 🧩 Modular Design

All major design tokens are declared as CSS variables for easy customization.  
This allows you to change typography, colors, and spacing globally without rewriting component styles.

### Most Commonly Edited Variables

#### 🎨 Colors  
Generated with [Realtime Colors](https://www.realtimecolors.com)

`css
--contrast: light-dark(#0d0d0a, #f6f7f4);
--background: light-dark(#c8ffcd, #0d0d0a);
--primary: #1c8f44;
--secondary: #067128;
--accent: #58f08b;`

### 🧱 Textures

From [Transparent Textures](https://www.transparenttextures.com/)

`css
--background-texture: url("https://www.transparenttextures.com/patterns/asfalt-light.png");`

### ✍️ Typography

Font stack and fluid type scale generated via [Utopia Type Calculator](https://utopia.fyi/type/calculator).  

#### Font Families

`--font-sans: "Roboto", system-ui, -apple-system, "Segoe UI", sans-serif;
--font-serif: "Roboto Serif", "Times New Roman", serif;`


#### Type Scale

`
--step--2: clamp(0.7035rem, 0.8117rem + -0.1353vw, 0.7813rem);
--step--1: clamp(0.9375rem, 0.9374rem + 0.0004vw, 0.9377rem);
--step-0: clamp(1.125rem, 1.0761rem + 0.2174vw, 1.25rem);
--step-1: clamp(1.35rem, 1.2263rem + 0.55vw, 1.6663rem);
--step-2: clamp(1.62rem, 1.3848rem + 1.0454vw, 2.2211rem);
--step-3: clamp(1.944rem, 1.5461rem + 1.7682vw, 2.9607rem);
--step-4: clamp(2.3328rem, 1.7013rem + 2.8067vw, 3.9467rem);
--step-5: clamp(2.7994rem, 1.8361rem + 4.281vw, 5.2609rem);

--heading-line-height: 1.12;
--heading-character-spacing: -0.075rem;
--body-line-height: 1.5; `

## 🪶 Logo
`--logo: url("data:image/svg+xml,%3Csvg fill='none' xmlns='http://www.w3.org/2000/svg' width='100%25' height='100%25' viewBox='0 0 24 24'%3E%3Cg id='SVGRepo_bgCarrier' stroke-width='0'/%3E%3Cg id='SVGRepo_tracerCarrier' stroke-linecap='round' stroke-linejoin='round'/%3E%3Cg id='SVGRepo_iconCarrier'%3E%3Cpath d='M8 4V20M17 12V20M6 20H10M15 20H19M13 7V4H3V7M21 14V12H13V14' stroke='%23c52f21' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/g%3E%3C/svg%3E");`

## 🧱 Project Structure
- index.html
- styles/
  - base.css
  - tokens.css
  - components/
    - header.css
    - carousel.css
- components/
  - (HTML sections)
- images/
  - (carousel and assets)

## 🚀 Getting Started

1. Clone the repository
    - git clone https://github.com/jaymaxco/HTML-Utopia-Project.git

2. Open index.html in your browser.

3. Adjust global variables in styles.css to match your brand or design palette.

## ⚙️ Customization Tips

- Modify color and typography variables in styles.css.

- Generate new type scales with utopia.fyi/type/calculator.

- Replace the texture URL or SVG logo as needed.

- Keep component CSS linked to variables, not hardcoded values.

## ⚖️ Limitations

- The CSS-only carousel supports auto-rotation only (no manual controls).

- Requires modern browsers that support clamp() and CSS variables.

- Media queries can still be added for complex layouts.

## 🧠 Resources

[Utopia — Fluid Type & Space Calculator](https://utopia.fyi/)

[Realtime Colors](https://www.realtimecolors.com/)

[Transparent Textures](https://www.transparenttextures.com/)

## 🔮 Future Enhancements

- Expand variable token set (layout, animation, transitions).

- Build a reusable component library (cards, buttons, grids).

- Add documentation pages with live examples.

License: MIT
Author: Jay Maxwell