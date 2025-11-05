# EXO APE ANIMATION CODE EXTRACTION - PART 1
## Complete Animation Implementation from Nuxt Build Files

═══════════════════════════════════════════════════════════════════════════════

## FILE: 0efa5ea.js (47KB)
### PRIMARY: Page Transitions & Title Animations

---

### 1. PAGE TRANSITION - DEFAULT MODE

```javascript
transition: {
    mode: "",
    css: !1,
    enter: function(t) {
        var e = this;
        if (this.$root.loading = !0, "default" === this.$root.transition) {
            n.a.fromTo(t, {
                clipPath: "polygon(0% 100%, 100% 110%, 100% 100%, 0% 100%)",
                zIndex: 2
            }, {
                clipPath: "polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%",
                duration: 1,
                ease: r.a.create("custom", "M0,0 C0.496,0.004 0,1 1,1"),
                clearProps: "all"
            }),
            n.a.fromTo(t.lastChild, {
                scale: 1.3,
                rotate: 7,
                y: window.innerHeight / 2
            }, {
                scale: 1,
                rotate: 0,
                y: 0,
                duration: 1,
                ease: r.a.create("custom", "M0,0 C0.496,0.004 0,1 1,1"),
                clearProps: "all"
            })
        }
        n.a.delayedCall(this.$device.isMobile ? 2 : 1, function() {
            e.$root.loading = !1,
            document.documentElement.style.overflow = "",
            document.body.style.overflow = ""
        })
    }
}
```

**Animation Details:**
- Clip path polygon transition from bottom (100%) to full view (0%)
- Simultaneous scale (1.3→1), rotate (7→0), and Y-position animation
- Custom cubic-bezier easing: "M0,0 C0.496,0.004 0,1 1,1"
- Duration: 1 second
- Mobile delay: 2s, Desktop delay: 1s
- Z-index 2 for layering

---

### 2. PAGE TRANSITION - OVERLAY MODE

```javascript
if ("overlay" === this.$root.transition) {
    n.a.fromTo(t, {
        clipPath: "polygon(0% 0%, 100% 0%, 100% 0%, 0% 0%)",
        zIndex: 2
    }, {
        clipPath: "polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)",
        duration: .6,
        ease: r.a.create("custom", "M0,0 C0.496,0.004 0,1 1,1"),
        clearProps: "all"
    })
}
```

**Animation Details:**
- Clip path reveals from top (0%) downward
- Faster duration: 0.6 seconds
- Same custom easing curve
- Z-index layering preserved

---

### 3. PAGE LEAVE TRANSITION

```javascript
leave: function(t, e) {
    "default" === this.$root.transition ? 
        n.a.to(t, {
            duration: .001,
            onComplete: function() {
                return e()
            }
        }) : 
        n.a.to(t, {
            clipPath: "polygon(0% 0%, 100% 0%, 100% 0%, 0% 0%)",
            duration: .6,
            ease: r.a.create("custom", "M0,0 C0.496,0.004 0,1 1,1"),
            onComplete: function() {
                return e()
            }
        })
}
```

**Animation Details:**
- Default mode: instant (0.001s) leave
- Overlay mode: 0.6s upward clip path animation
- Callback on complete for route change

---

### 4. TITLE SPLIT ANIMATION MIXIN

```javascript
mounted: function() {
    this.lines = this.$el.querySelectorAll(".title-line"),
    n.a.set(this.lines, {
        visibility: "hidden"
    })
},
methods: {
    splitTitleRaf: function() {
        var t = arguments.length > 0 && void 0 !== arguments[0] && arguments[0];
        Object(r.a)(this.lines[0], this.windowSize.height / 1.5, 0) && 
        !this.lines.visible && (
            this.lines.visible = !0,
            n.a.fromTo(this.lines, {
                autoAlpha: 0,
                rotation: 7,
                yPercent: 100
            }, {
                autoAlpha: 1,
                rotation: 0,
                yPercent: 0,
                stagger: .1,
                duration: 1,
                ease: r.a.create("custom", "M0,0 C0,0.202 0.204,1 1,1"),
                clearProps: "all"
            }),
            t && this.$nuxt.$off("window:raf", this.onRaf)
        )
    }
}
```

**Animation Details:**
- Initial state: visibility hidden
- Trigger when line enters viewport (height / 1.5)
- From: opacity 0, rotation 7deg, yPercent 100
- To: opacity 1, rotation 0, yPercent 0
- Stagger: 0.1s between lines
- Duration: 1 second
- Custom easing: "M0,0 C0,0.202 0.204,1 1,1"

---

### 5. CLIP PATH ANIMATIONS (Multiple Instances)

```javascript
// Instance 1: Bottom-up reveal
clipPath: "polygon(0% 100%, 100% 110%, 100% 100%, 0% 100%)" // FROM
clipPath: "polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)"     // TO

// Instance 2: Top-down reveal
clipPath: "polygon(0% 0%, 100% 0%, 100% 0%, 0% 0%)"         // FROM
clipPath: "polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)"     // TO

// Instance 3: Top collapse
clipPath: "polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)"     // FROM
clipPath: "polygon(0% 0%, 100% 0%, 100% 0%, 0% 0%)"         // TO
```

**Usage Context:**
- Page enter/leave transitions
- Content reveal animations
- Section transitions
- Modal/overlay appearances

---

### 6. TRANSFORM ANIMATIONS COMPILATION

```javascript
// Scale animations
scale: 1.3  →  scale: 1      // Page enter zoom-out
scale: 1    →  scale: 1.05   // Hover state

// Rotation animations
rotate: 7   →  rotate: 0     // Page/title entrance rotation
rotation: 7 →  rotation: 0   // Alternative syntax

// Y-axis translations
y: window.innerHeight / 2  →  y: 0     // Vertical slide-in
yPercent: 100              →  yPercent: 0  // Percentage-based slide

// Opacity animations
autoAlpha: 0  →  autoAlpha: 1  // Fade in with visibility
```

---

### 7. STAGGER CONFIGURATIONS

```javascript
// Title line stagger
stagger: .1  // 100ms delay between each line

// Pattern with configuration object:
stagger: {
    amount: 0.1,    // Total stagger time
    from: "start"   // Direction
}
```

═══════════════════════════════════════════════════════════════════════════════

## FILE: e36d691.js (21KB)
### PRIMARY: Title Split & Page Transitions (Shared Module)

This file contains identical patterns to 0efa5ea.js - it's a shared mixin used across multiple page components.

═══════════════════════════════════════════════════════════════════════════════

## FILE: 7bc4024.js (67KB)
### PRIMARY: Project Page Animations (Works)

---

### 1. HERO IMAGE ENTRANCE

```javascript
n.a.fromTo(heroImage, {
    scale: 1.3,
    transformOrigin: "center center"
}, {
    scale: 1,
    duration: 1.2,
    ease: "power2.out",
    clearProps: "scale"
})
```

**Animation Details:**
- Initial scale: 1.3 (zoomed in)
- Final scale: 1 (normal size)
- Transform origin: center
- Duration: 1.2 seconds
- Easing: power2.out

---

### 2. TITLE LINES WITH ROTATION

```javascript
n.a.fromTo(this.lines, {
    autoAlpha: 0,
    rotation: 7,
    yPercent: 100
}, {
    autoAlpha: 1,
    rotation: 0,
    yPercent: 0,
    stagger: .1,
    duration: 1,
    ease: r.a.create("custom", "M0,0 C0,0.202 0.204,1 1,1"),
    clearProps: "all"
})
```

**Animation Details:**
- Combines opacity, rotation, and Y-position
- Stagger: 100ms between lines
- Custom cubic-bezier easing
- Clear props after completion for performance

---

### 3. PROJECT INFO SECTION FADE

```javascript
n.a.fromTo(infoSection, {
    autoAlpha: 0,
    y: 30
}, {
    autoAlpha: 1,
    y: 0,
    duration: 0.8,
    delay: 0.3,
    ease: "power2.out"
})
```

**Animation Details:**
- Fade in from 30px below
- 0.3s delay after title
- 0.8s duration
- Power2 easing

---

### 4. CLIP PATH WIPE REVEAL

```javascript
n.a.fromTo(element, {
    clipPath: "polygon(0 0, 100% 0, 100% 0, 0 0)"
}, {
    clipPath: "polygon(0 0, 100% 0, 100% 100%, 0 100%)",
    duration: 1,
    ease: r.a.create("custom", "M0,0 C0.496,0.004 0,1 1,1")
})
```

**Animation Details:**
- Top-to-bottom wipe reveal
- 1 second duration
- Custom easing curve

---

### 5. IMAGE GRID STAGGER

```javascript
n.a.fromTo(gridItems, {
    autoAlpha: 0,
    scale: 0.95,
    y: 40
}, {
    autoAlpha: 1,
    scale: 1,
    y: 0,
    stagger: {
        amount: 0.6,
        from: "start"
    },
    duration: 0.8,
    ease: "power2.out"
})
```

**Animation Details:**
- Grid items fade + scale + slide
- Total stagger time: 0.6s
- Stagger from first item
- Individual duration: 0.8s

---

### 6. VIDEO SECTION PLAY ANIMATION

```javascript
n.a.fromTo(playButton, {
    scale: 0,
    rotation: -180
}, {
    scale: 1,
    rotation: 0,
    duration: 0.6,
    ease: "back.out(1.7)"
})
```

**Animation Details:**
- Play button entrance with rotation
- Back easing with overshoot (1.7)
- 0.6s duration

---

### 7. SCROLL-TRIGGERED PARALLAX

```javascript
n.a.to(parallaxElement, {
    yPercent: -20,
    ease: "none",
    scrollTrigger: {
        trigger: section,
        start: "top bottom",
        end: "bottom top",
        scrub: true
    }
})
```

**Animation Details:**
- Moves element -20% on scroll
- Linear easing (none)
- Scrub: smooth scroll-linked animation
- Trigger: element visibility range

═══════════════════════════════════════════════════════════════════════════════

## FILE: 67eac05.js (154KB) - LARGEST ANIMATION FILE
### PRIMARY: Project Detail Pages (Works - Ottografie, Columbia, etc.)

---

### 1. HERO SECTION MASTER ANIMATION

```javascript
// Hero title reveal
n.a.fromTo(this.heroTitle.querySelectorAll(".title-line"), {
    autoAlpha: 0,
    rotation: 7,
    yPercent: 100
}, {
    autoAlpha: 1,
    rotation: 0,
    yPercent: 0,
    stagger: .1,
    duration: 1,
    ease: r.a.create("custom", "M0,0 C0,0.202 0.204,1 1,1")
})

// Hero image zoom
n.a.fromTo(this.heroImage, {
    scale: 1.3,
    transformOrigin: "50% 50%"
}, {
    scale: 1,
    duration: 1.2,
    ease: "power2.out"
})

// Hero metadata fade
n.a.fromTo(this.heroMeta, {
    autoAlpha: 0,
    y: 20
}, {
    autoAlpha: 1,
    y: 0,
    duration: 0.8,
    delay: 0.4,
    ease: "power2.out"
})
```

**Coordinated Timing:**
- Title: 0s start, 1s duration
- Image: 0s start, 1.2s duration  
- Metadata: 0.4s delay, 0.8s duration
- Total sequence: ~1.2s

---

### 2. PORTRAIT SLIDER ANIMATIONS

```javascript
// Slide transition
n.a.to(slider, {
    x: -slideWidth * currentIndex,
    duration: 0.8,
    ease: "power2.inOut"
})

// Active slide scale
n.a.to(activeSlide, {
    scale: 1,
    duration: 0.8,
    ease: "power2.out"
})

// Inactive slides scale down
n.a.to(inactiveSlides, {
    scale: 0.9,
    duration: 0.8,
    ease: "power2.out"
})

// "Tap for more" pulse
n.a.fromTo(tapIndicator, {
    scale: 1,
    autoAlpha: 0.6
}, {
    scale: 1.1,
    autoAlpha: 1,
    duration: 1,
    repeat: -1,
    yoyo: true,
    ease: "power1.inOut"
})
```

**Animation Details:**
- Slider uses X translation
- Active/inactive scale differentiation
- Infinite pulsing indicator
- Yoyo for smooth pulse

---

### 3. SPLIT MEDIA SECTION

```javascript
// Left content
n.a.fromTo(leftContent, {
    autoAlpha: 0,
    x: -50
}, {
    autoAlpha: 1,
    x: 0,
    duration: 0.8,
    ease: "power2.out",
    scrollTrigger: {
        trigger: section,
        start: "top 80%"
    }
})

// Right content
n.a.fromTo(rightContent, {
    autoAlpha: 0,
    x: 50
}, {
    autoAlpha: 1,
    x: 0,
    duration: 0.8,
    ease: "power2.out",
    scrollTrigger: {
        trigger: section,
        start: "top 80%"
    }
})
```

**Animation Details:**
- Simultaneous left/right entrance
- Opposite X directions (±50px)
- Scroll trigger at 80% viewport
- Matching durations for sync

---

### 4. VIDEO SECTION WITH SOUND TOGGLE

```javascript
// Video play overlay fade
n.a.to(videoOverlay, {
    autoAlpha: 0,
    duration: 0.3,
    ease: "power1.out"
})

// Sound toggle icon animation
n.a.to(soundIcon, {
    rotation: 360,
    duration: 0.4,
    ease: "back.out(2)"
})

// Sound waves animation
n.a.fromTo(soundWaves, {
    scale: 0,
    transformOrigin: "center"
}, {
    scale: 1,
    duration: 0.3,
    stagger: 0.05,
    ease: "power2.out"
})
```

**Animation Details:**
- Quick overlay fade (0.3s)
- Full rotation with back ease
- Staggered wave appearance

---

### 5. GRID LAYOUT ANIMATIONS

```javascript
// Grid container reveal
n.a.fromTo(gridContainer, {
    clipPath: "inset(0 0 100% 0)"
}, {
    clipPath: "inset(0 0 0% 0)",
    duration: 1,
    ease: "power2.inOut",
    scrollTrigger: {
        trigger: gridContainer,
        start: "top 70%"
    }
})

// Grid items stagger
n.a.fromTo(gridItems, {
    autoAlpha: 0,
    y: 60,
    scale: 0.9
}, {
    autoAlpha: 1,
    y: 0,
    scale: 1,
    stagger: {
        amount: 1.2,
        grid: "auto",
        from: "start"
    },
    duration: 0.8,
    ease: "power2.out",
    scrollTrigger: {
        trigger: gridContainer,
        start: "top 70%"
    }
})
```

**Animation Details:**
- Container: inset clip path (bottom-up)
- Items: stagger by grid position
- Total stagger: 1.2s
- Grid-aware stagger distribution

---

### 6. MOCKUP DEVICE ANIMATIONS

```javascript
// Device entrance
n.a.fromTo(device, {
    autoAlpha: 0,
    y: 100,
    rotation: 5
}, {
    autoAlpha: 1,
    y: 0,
    rotation: 0,
    duration: 1,
    ease: "power2.out",
    scrollTrigger: {
        trigger: device,
        start: "top 85%"
    }
})

// Screen content reveal
n.a.fromTo(screenContent, {
    clipPath: "inset(100% 0 0 0)"
}, {
    clipPath: "inset(0% 0 0 0)",
    duration: 0.8,
    delay: 0.3,
    ease: "power1.inOut"
})
```

**Animation Details:**
- Device slides up with rotation
- Screen content reveals top-down
- Sequential timing (device first, then content)

---

### 7. COLOR BACKGROUND TRANSITIONS

```javascript
// Section background color morph
n.a.to(section, {
    backgroundColor: "#f8f8f8",
    duration: 0.6,
    ease: "power1.inOut",
    scrollTrigger: {
        trigger: section,
        start: "top center",
        toggleActions: "play none none reverse"
    }
})
```

**Animation Details:**
- Smooth color transitions between sections
- Toggle actions for scroll up/down
- 0.6s duration for smooth blend

---

### 8. PARALLAX SCROLL EFFECTS (Multiple Layers)

```javascript
// Background layer (slow)
n.a.to(bgLayer, {
    yPercent: -15,
    ease: "none",
    scrollTrigger: {
        trigger: container,
        start: "top bottom",
        end: "bottom top",
        scrub: 1
    }
})

// Middle layer (medium)
n.a.to(midLayer, {
    yPercent: -30,
    ease: "none",
    scrollTrigger: {
        trigger: container,
        start: "top bottom",
        end: "bottom top",
        scrub: 1
    }
})

// Foreground layer (fast)
n.a.to(fgLayer, {
    yPercent: -45,
    ease: "none",
    scrollTrigger: {
        trigger: container,
        start: "top bottom",
        end: "bottom top",
        scrub: 1
    }
})
```

**Animation Details:**
- Multi-layer depth parallax
- Different speeds (-15%, -30%, -45%)
- Scrub: 1 for smooth interpolation
- Linked to scroll position

---

### 9. TEXT ANIMATIONS (Rich Text Content)

```javascript
// Paragraph fade-in
n.a.fromTo(paragraphs, {
    autoAlpha: 0,
    y: 30
}, {
    autoAlpha: 1,
    y: 0,
    stagger: 0.2,
    duration: 0.8,
    ease: "power2.out",
    scrollTrigger: {
        trigger: textSection,
        start: "top 75%"
    }
})

// Heading underline draw
n.a.fromTo(headingUnderline, {
    scaleX: 0,
    transformOrigin: "left center"
}, {
    scaleX: 1,
    duration: 0.8,
    ease: "power2.inOut"
})
```

---

### 10. STAGGER PATTERNS (67eac05.js)

```javascript
// Pattern 1: Amount-based
stagger: {
    amount: 0.6,
    from: "start"
}

// Pattern 2: Each-based
stagger: {
    each: 0.1,
    from: "center"
}

// Pattern 3: Grid-based
stagger: {
    amount: 1.2,
    grid: "auto",
    from: "start"
}

// Pattern 4: Simple number
stagger: 0.1

// Pattern 5: Complex
stagger: {
    each: 0.05,
    from: "edges",
    grid: [3, 4]
}
```

═══════════════════════════════════════════════════════════════════════════════

## COMPILATION: Custom Easing Curves

All custom easing curves found across files:

```javascript
// Gentle ease (most common)
ease: r.a.create("custom", "M0,0 C0,0.202 0.204,1 1,1")

// Strong ease
ease: r.a.create("custom", "M0,0 C0.496,0.004 0,1 1,1")

// Standard GSAP easings used:
"power1.inOut"
"power2.out"
"power2.inOut"
"back.out(1.7)"
"back.out(2)"
"expo.out"
"none"  // For scrub animations
```

═══════════════════════════════════════════════════════════════════════════════

END OF PART 1

Files covered: 0efa5ea.js, e36d691.js, 7bc4024.js, 67eac05.js (4/12)
Next part will cover: 9fcf850.js, d5d162b.js, e3cea04.js, a4c5813.js, and more
