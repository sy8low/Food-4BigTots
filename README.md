# Food-4BigTots ![Food-4BigTots logo](food4bigtots/static/media/theme/FFT_icon_nobg.png)

**[Food-4BigTots](https://www.food-4bigtots.xyz/)** is a tribute to my mum’s food blog, **[Food-4Tots](https://food-4tots.com/)**.

I took up this project to relive my sweet childhood memories of helping my mum with the blog (testing food and modelling for photos 😁), and to continue its mission of helping everyone make simple, healthy food that also tastes really good. 😋

* Click **[here](https://www.food-4bigtots.xyz/about/)** to read our story!

* Click **[here](https://youtu.be/5aG8SreoxTM?si=9ckqu47DKdCIV6HR)** to watch my Youtube video explaining the project.

* Click **[here](food4bigtots/)** to view the source code for the project.

I set out to redesign **[Food-4Tots](https://food-4tots.com/)**:

* The original blog is built on a clunky, rudimental **WordPress template**. It is also covered with advertisements that often disrupt the layout and UX (user experience). I wanted the new blog to have all the old favorites; no advertisements; and a **clean, modern layout**.

* Furthermore, the original blog is a **static website**, and all the content is hardcoded. I wanted the new blog to be a **dynamic web app**, designed to be scalable and flexible.

**[Food-4BigTots](https://www.food-4bigtots.xyz/)** is built on the **“MVC”** paradigm. It has:

* A **“Model”**: a database containing information about the recipes in the blog;

* A **“View”**: the frontend UI (user interface) and content that users interact with; and

* A **“Controller”**: the backend server connecting the Model to the View.

## Model (Database)
Click **[here](food4bigtots/schema.sql)** to view the database's schema (structure).

### 🖇️ Relational Database (SQL, SQLite)
* Data about recipes and categories are stored in separate tables, and each entry has its own ID (identification) number, called a **Primary Key**.

* The recipes are then mapped to categories via a **mapping** table, which references their respective IDs as **Foreign Keys**.

* The ID and name columns of both tables are **indexed**, which optimizes them for searching.

## View (Frontend)

### 📜 Templates (HTML, Jinja)
Since all my **HTML** pages share a similar layout, I wrote them as **templates** using **Jinja**.

Click **[here](food4bigtots/templates)** to view the templates.

* I created a **base template**, which houses the header; footer; navigation bar; and common metadata, stylesheets, and scripts.

* I built a **recipe template** on top of it to standardize the layout of my recipe pages.

* Every page (referred to as **child templates**) builds upon either one of these two **parent templates**.

#### Variables & Blocks
* The parent templates contain many **variables** and **blocks**, which can be set or overridden by child templates or the backend controller to generate a complete HTML page.

* This keeps my markup **DRY (Don’t Repeat Yourself)**, as there is no duplicate content in my templates.

#### Macros
* I implemented features used throughout my app as Jinja **macros**, which are reusable snippets of HTML (analogous to Python’s functions), and parked them in a separate template.

* This not only makes my markup DRY, **modular**, and easy to maintain, but also less prone to bugs, as the behavior of these features is standardized.

* These features include:
    * The **gallery** in my Home page and category pages;

    * The **tiles** that make up the gallery;

    * The **double column layout** used in most pages, which has a static left pane for text and a sticky right pane for images (i.e. the image stays at the same position on the screen while you scroll through the text);

    * The **accordions** showing the steps in the recipe pages, which you can click to open and close; and

    * The **ingredient checklists** in the recipe pages.

### 💅 Styling
Click **[here](food4bigtots/static/scss/styles.scss)** to view the my custom pre-compiled SASS stylesheet (both my custom SASS stylesheet and the one provided by Bootstrap were compiled into a single CSS stylesheet, which is used to style pages).

Styling was the most challenging part of this project. 😵‍💫

#### Bootstrap Utility Classes & Custom CSS Stylesheet
* I like **Bootstrap’s utility classes**, as they offer great convenience and are neater than inline styling and IDs.

* However, I reserved them for isolated cases, as I wanted to follow to the **best practices** of placing CSS in separate custom stylesheets (separation of concerns) and applying CSS declarations to groups of elements collectively rather than individually.

* Using **custom stylesheets** also gave me finer control over the values of CSS properties compared to Bootstrap’s defaults.

#### Customisation with SASS Variables
* When styling Bootstrap components in my custom stylesheet, I adhered rigorously to the principle of DRY styling by **overriding** Bootstrap’s defaults whenever possible.

* This was not feasible with the compiled CSS stylesheet provided by their CDN (Content Delivery Network). As such, I had to work with their pre-compiled **SASS** stylesheet locally.

* An advantage of using SASS is that their **variables** are more user-friendly than CSS’s native variables, which makes my stylesheet more **maintainable**.

#### Specificity & Cascading with SASS Nesting
* If overriding didn’t work, or if I needed to style a particular element, I used highly **specific** CSS selectors so that my declarations are applied over Bootstrap’s.

* Furthermore, SASS’s nesting feature made it easier to write highly specific selectors and eliminate redundant declarations by taking advantage of CSS’s **cascading** nature (another best practice).

### 🐍 Responsive UI
#### Bootstrap's Grid Layout & Breakpoints
* To make the UI responsive to **different screen sizes**, I used Bootstrap’s **grid layout** and placed page components into containers, rows, and columns. 

* With Bootstrap’s **breakpoints**, I set the page layout and the dimensions of page components to change according the current screen size (subsets of common device sizes and viewport dimensions).

* This allows my app to be displayed neatly without anything overflowing beyond the screen, no matter which device it is viewed on.

#### Relative Units
* Additionally, to make the UI responsive to different default font sizes and line spacing widths on **different browsers**, I took care to use only relative units, such as `rem` and `lh`.

* I used `%` and `vh` as well to account for **different screen sizes**.

#### Media Queries & DevTools
* I tested the responsiveness of my app rigorously using **Chrome DevTools** (Google Chrome’s built-in developer tools).

* During testing, I found that my error page was too short, and this resulted in a large white block being shown below the footer on devices with big screens.

* I corrected this by using CSS **media queries** to size the page differently for big and small screens.

### 👋 Interactive UI
The original **[Food-4Tots](https://food-4tots.com/)** page had interesting content and beautiful images, but it did not have an attractive UI. I wanted to make my app more engaging by making it more **interactive**.

#### Bootstrap JavaScript Plugins & Components
* Bootstrap’s compiled **JavaScript plugin** provided me with many ready-made interactive components, such as the **clickable accordion** you saw earlier.

* Another one is the **offcanvas pane**, which I used to build a navigation bar that can be hidden.

#### JavaScript & jQuery Event Listeners
Click **[here](food4bigtots/static/js/interactive.js)** to view my custom script.

However, I had to make the gallery interactive on my own using **jQuery** and **JavaScript**.

* I attached **event listeners** to the tiles to detect mouse hovers.

* When the user’s mouse enters a tile, the thumbnail will become a link to the corresponding recipe; when it leaves, the thumbnail will return.

* This is achieved by the **callback function** passed into the event listener which toggles the Bootstrap classes on the tiles that control their CSS display properties.

### 🌎 Sharing
#### Open Graph Tags
* I hope to use **[Food-4BigTots](https://www.food-4bigtots.xyz/)** to share my family’s love for cooking, and convince everyone that making healthy and delicious food is quite easy. 🥰

* To help it leave a stronger impression, I utilized **Open Graph tags** to design **rich previews** that will show up when my app is shared on social media and messaging platforms.

## Controller (Backend)
Click **[here](food4bigtots/)** to view the source code for the backend.

### 🔭 View Functions & Error Handlers (Flask, Python)
When the **Flask** app receives a HTTP **request** from a visitor, it matches the incoming request URL to the correct **view function** to be handled.

* For example, if the user visits (i.e. requests for) a category page, the request will be passed to the view function for category pages, which generates a **response** to be sent to the user by **rendering the correct template**.

* If the user visits a recipe page, a similar process is followed, except that the request will be handled by the view function for recipe pages.

* However, if the URL cannot be matched to any view function, or a template cannot be found, it will be handled by an **error handler**, which renders an error page instead.

### 📦 Variable URL Rules, Stateful URLs
* Since my app has many pages that need to be rendered through the same process, and the incoming URLs are **stateful** (i.e. contain information about which page the user is requesting for), I allowed the view functions to take **variable URL rules**.

* This means that they take the components of the URL as **arguments** (i.e. inputs), and use them to find the correct template to be rendered.

* Since one view function can handle any requests for one type of page, my code can be kept DRY (i.e. minimal duplication) and **scalable** to accommodate new pages with no changes.

### ❓ sqlite3 Queries
* These arguments are also passed into **queries** of the database using **Python’s** built-in **sqlite3** library.

* The database returns **metadata** about the recipe or category, such as its properly capitalized title, date of publication, the filename of its thumbnail, and the original **[Food-4Tots](https://food-4tots.com/)** page.

* These are all passed into templates to set the values of **variables**.

### 🛣️ Jinja Filters & Flask Path Builders
* To automatically generate links to pictures and pages on my app, I used **Flask’s file path builder function** and my **custom Jinja filters**.

* By minimizing **hardcoded** information in the templates, I made the frontend more flexible and resilient to changes.

### 🍪 Cookies
* The list of categories in the navigation bar and footer are dynamically rendered by querying the database.

* However, since these features appear on every page, my app will be slowed down by repeated querying, and computational resources will be wasted.

* To address this, I designed the app to store this data in a filesystem **cookie** when the user first visits the app, and retrieve it whenever a new page is rendered.

## Hosting & Version Control
Finally, to make **[Food-4BigTots](https://www.food-4bigtots.xyz/)** available on the internet, I **hosted** it on **PythonAnywhere**.

### Why I chose them
* The most **straightforward** hosting process;

* **Adequate features** for simple web apps; and

* A **permanent filesystem** (in contrast with the ephemeral filesystems of Heroku and Render, which will wipe out my files, particularly my local SQLite database, every time I restart the app).

### The hosting process
* I used **Git** to copy my app’s source code, templates, and static files from my **GitHub remote repository** to their server.

* Since my SQLite database is not in the repository, I had to copy it over separately using **SSH** (Secure Shell Protocol).

And with this, **[Food-4Tots’](https://food-4tots.com/)** new chapter began!

## 💖 Show Us Some Love! 
Do give **[Food-4BigTots](https://www.food-4bigtots.xyz/)** and **[Food-4Tots](https://food-4tots.com/)** a visit, my mum and I would really appreciate your support!

If you like our blogs or if there’s any recipe on **[Food-4Tots](https://food-4tots.com/)** that you’d like me to bring over to **[Food-4BigTots](https://www.food-4bigtots.xyz/)**, feel free to leave a comment on my **[Youtube video](https://youtu.be/5aG8SreoxTM?si=9ckqu47DKdCIV6HR)** or reach out to us via our socials!

* FFT's **[email](mailto:foodfortots@yahoo.com)**

* FFT's **[Facebook page](https://www.facebook.com/FoodForToddlers)**

* SY's **[LinkedIn](https://www.linkedin.com/in/sze-yoong-low-b52438210/)**
