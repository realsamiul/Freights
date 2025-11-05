# EXO APE ANIMATION CODE EXTRACTION - PART 2
## Complete Animation Implementation from Nuxt Build Files (Continued)

═══════════════════════════════════════════════════════════════════════════════

## FILE: 9fcf850.js (27KB)
### PRIMARY: CSS Custom Properties & Base Animations

---

### 1. LOADER/PRELOADER ANIMATIONS

```javascript
// Loader circle animation
n.a.fromTo(loaderCircle, {
    strokeDashoffset: 0,
    rotation: -90,
    transformOrigin: "center center"
}, {
    strokeDashoffset: -circumference,
    rotation: 270,
    duration: 2,
    ease: "power2.inOut",
    repeat: -1
})

// Loader fade out
n.a.to(loaderContainer, {
    autoAlpha: 0,
    duration: 0.6,
    delay: 0.5,
    ease: "power2.out",
    onComplete: function() {
        loaderContainer.style.display = "none"
    }
})
```

**Animation Details:**
- SVG circle stroke animation (dashoffset technique)
- Rotation from -90deg to 270deg (full rotation)
- Infinite repeat for loading state
- Fade out on page load complete

---

### 2. NAVIGATION ANIMATIONS

```javascript
// Menu open animation
n.a.fromTo(menuOverlay, {
    clipPath: "circle(0% at top right)"
}, {
    clipPath: "circle(150% at top right)",
    duration: 0.8,
    ease: "power3.inOut"
})

// Menu items stagger
n.a.fromTo(menuItems, {
    autoAlpha: 0,
    y: 30,
    rotation: -5
}, {
    autoAlpha: 1,
    y: 0,
    rotation: 0,
    stagger: 0.08,
    duration: 0.6,
    delay: 0.3,
    ease: "power2.out"
})

// Menu close animation
n.a.to(menuOverlay, {
    clipPath: "circle(0% at top right)",
    duration: 0.6,
    ease: "power3.inOut"
})
```

**Animation Details:**
- Circular reveal from top-right corner
- Staggered menu item entrance (80ms between items)
- Items have subtle rotation on entrance
- Reverse circular collapse on close

---

### 3. BURGER MENU ICON ANIMATION

```javascript
// Top line
n.a.to(burgerLineTop, {
    y: 6,
    rotation: 45,
    transformOrigin: "center",
    duration: 0.3,
    ease: "power2.inOut"
})

// Middle line
n.a.to(burgerLineMiddle, {
    autoAlpha: 0,
    duration: 0.1
})

// Bottom line
n.a.to(burgerLineBottom, {
    y: -6,
    rotation: -45,
    transformOrigin: "center",
    duration: 0.3,
    ease: "power2.inOut"
})
```

**Animation Details:**
- Transforms hamburger → X
- Top/bottom lines rotate ±45deg
- Middle line fades out instantly
- 0.3s duration for smooth transition

---

### 4. SCROLL INDICATOR ANIMATION

```javascript
// "Scroll to explore" fade loop
n.a.fromTo(scrollIndicator, {
    autoAlpha: 0.5,
    y: 0
}, {
    autoAlpha: 1,
    y: 10,
    duration: 1.2,
    repeat: -1,
    yoyo: true,
    ease: "power1.inOut"
})

// Arrow bounce
n.a.to(scrollArrow, {
    y: 5,
    duration: 0.8,
    repeat: -1,
    yoyo: true,
    ease: "power1.inOut"
})
```

**Animation Details:**
- Infinite loop with yoyo (bounce effect)
- Opacity pulse + Y-movement
- Separate arrow animation for emphasis
- Attracts attention to scroll action

═══════════════════════════════════════════════════════════════════════════════

## FILE: d5d162b.js (130KB)
### PRIMARY: Homepage & Featured Projects

---

### 1. HERO TITLE ENTRANCE (Homepage)

```javascript
// Main hero title animation
n.a.fromTo(heroTitle, {
    clipPath: "polygon(0 0, 100% 0, 100% 0, 0 0)",
    y: 100
}, {
    clipPath: "polygon(0 0, 100% 0, 100% 100%, 0 100%)",
    y: 0,
    duration: 1.2,
    ease: "power3.out"
})

// Title split lines
n.a.fromTo(titleLines, {
    autoAlpha: 0,
    yPercent: 100,
    rotation: 7
}, {
    autoAlpha: 1,
    yPercent: 0,
    rotation: 0,
    stagger: 0.12,
    duration: 1,
    delay: 0.2,
    ease: r.a.create("custom", "M0,0 C0,0.202 0.204,1 1,1")
})
```

**Animation Details:**
- Container: clip path top-to-bottom reveal
- Lines: staggered entrance with rotation
- 0.2s delay for choreography
- Total animation: ~1.3s

---

### 2. FEATURED PROJECT CARDS

```javascript
// Project card entrance
n.a.fromTo(projectCards, {
    autoAlpha: 0,
    y: 80,
    scale: 0.95
}, {
    autoAlpha: 1,
    y: 0,
    scale: 1,
    stagger: {
        amount: 0.8,
        from: "start"
    },
    duration: 1,
    ease: "power2.out",
    scrollTrigger: {
        trigger: projectsSection,
        start: "top 70%"
    }
})

// Hover effect
n.a.to(projectCard, {
    scale: 1.02,
    duration: 0.4,
    ease: "power2.out"
})

// Video thumbnail play on hover
n.a.to(videoThumbnail, {
    autoAlpha: 1,
    duration: 0.3
})
```

**Animation Details:**
- Cards enter with fade, slide, and scale
- Total stagger: 0.8s across all cards
- Hover: subtle scale increase (1.02)
- Video crossfade on hover

---

### 3. PROJECT THUMBNAIL VIDEO TRANSITION

```javascript
// Image to video crossfade
n.a.timeline()
    .to(thumbnailImage, {
        autoAlpha: 0,
        duration: 0.3,
        ease: "power1.out"
    }, 0)
    .fromTo(thumbnailVideo, {
        autoAlpha: 0
    }, {
        autoAlpha: 1,
        duration: 0.3,
        ease: "power1.in",
        onStart: function() {
            thumbnailVideo.play()
        }
    }, 0)

// Reverse on mouse leave
n.a.timeline()
    .to(thumbnailVideo, {
        autoAlpha: 0,
        duration: 0.2,
        onComplete: function() {
            thumbnailVideo.pause()
            thumbnailVideo.currentTime = 0
        }
    }, 0)
    .to(thumbnailImage, {
        autoAlpha: 1,
        duration: 0.2
    }, 0)
```

**Animation Details:**
- Simultaneous crossfade (timeline with position parameter 0)
- Video plays on fade-in
- Resets on mouse leave
- Quick transitions (0.2-0.3s)

---

### 4. SHOWREEL SECTION

```javascript
// Showreel container reveal
n.a.fromTo(showreelContainer, {
    clipPath: "inset(0 0 100% 0)"
}, {
    clipPath: "inset(0 0 0% 0)",
    duration: 1,
    ease: "power2.inOut",
    scrollTrigger: {
        trigger: showreelContainer,
        start: "top 75%"
    }
})

// Play button entrance
n.a.fromTo(playButton, {
    scale: 0,
    rotation: -90
}, {
    scale: 1,
    rotation: 0,
    duration: 0.8,
    delay: 0.5,
    ease: "back.out(1.7)"
})

// Play button pulse
n.a.to(playButtonCircle, {
    scale: 1.2,
    autoAlpha: 0,
    duration: 1.5,
    repeat: -1,
    ease: "power1.out"
})
```

**Animation Details:**
- Bottom-up inset clip reveal
- Play button with back ease (bounce)
- Infinite pulse ring for attention
- 0.5s delay after container reveal

---

### 5. NEWS/MEDIA SECTION HORIZONTAL SCROLL

```javascript
// Media wrapper scroll animation
n.a.to(mediaWrapper, {
    x: () => -(mediaWrapper.scrollWidth - window.innerWidth),
    ease: "none",
    scrollTrigger: {
        trigger: mediaSection,
        start: "top top",
        end: () => "+=" + (mediaWrapper.scrollWidth - window.innerWidth),
        scrub: 1,
        pin: true,
        anticipatePin: 1
    }
})

// Media items parallax within scroll
n.a.to(mediaItems, {
    y: (i) => -50 * (i % 2),  // Alternating parallax
    ease: "none",
    scrollTrigger: {
        trigger: mediaSection,
        start: "top top",
        end: () => "+=" + (mediaWrapper.scrollWidth - window.innerWidth),
        scrub: 1
    }
})
```

**Animation Details:**
- Horizontal scroll triggered by vertical scroll
- Dynamic end calculation based on content width
- Section pinning during scroll
- Individual item parallax within scroll

---

### 6. FOOTER REVEAL ANIMATION

```javascript
// Footer slide up
n.a.fromTo(footer, {
    y: 100,
    autoAlpha: 0
}, {
    y: 0,
    autoAlpha: 1,
    duration: 0.8,
    ease: "power2.out",
    scrollTrigger: {
        trigger: footer,
        start: "top 90%"
    }
})

// Footer links stagger
n.a.fromTo(footerLinks, {
    autoAlpha: 0,
    y: 20
}, {
    autoAlpha: 1,
    y: 0,
    stagger: 0.05,
    duration: 0.6,
    delay: 0.3,
    ease: "power2.out"
})
```

**Animation Details:**
- Footer enters from below
- Links stagger after footer appears
- Quick stagger (50ms between links)

---

### 7. IMAGE LAZY LOAD ANIMATIONS

```javascript
// Image fade in on load
n.a.fromTo(lazyImage, {
    autoAlpha: 0,
    scale: 1.1
}, {
    autoAlpha: 1,
    scale: 1,
    duration: 0.8,
    ease: "power2.out"
})
```

**Animation Details:**
- Subtle zoom-out effect (1.1 → 1)
- Fade in simultaneously
- Triggered on image load event

---

### 8. CTA BUTTON ANIMATIONS

```javascript
// Button circle fill on hover
n.a.to(buttonCircle, {
    scale: 1,
    duration: 0.5,
    ease: "power2.out"
})

// Button text slide
n.a.to(buttonText, {
    x: 10,
    duration: 0.3,
    ease: "power2.out"
})

// Button arrow rotation
n.a.to(buttonArrow, {
    rotation: 45,
    duration: 0.3,
    ease: "power2.out"
})
```

**Animation Details:**
- Circle scales from center
- Text shifts right slightly
- Arrow rotates 45deg
- All choreographed on hover

═══════════════════════════════════════════════════════════════════════════════

## FILE: e3cea04.js (62KB)
### PRIMARY: Studio Page Animations

---

### 1. SERVICES SECTION IMAGE COLUMNS

```javascript
// Left column - slower parallax
n.a.to(leftImageColumn, {
    yPercent: -10,
    ease: "none",
    scrollTrigger: {
        trigger: servicesSection,
        start: "top bottom",
        end: "bottom top",
        scrub: 1.5
    }
})

// Right column - faster parallax
n.a.to(rightImageColumn, {
    yPercent: -25,
    ease: "none",
    scrollTrigger: {
        trigger: servicesSection,
        start: "top bottom",
        end: "bottom top",
        scrub: 1.5
    }
})
```

**Animation Details:**
- Different parallax speeds for depth
- Scrub 1.5 for smoother motion
- Full viewport range (top bottom → bottom top)

---

### 2. STUDIO TITLE SEQUENCE

```javascript
// "Studio" word reveal
n.a.fromTo(studioTitle, {
    clipPath: "polygon(0 100%, 100% 100%, 100% 100%, 0 100%)"
}, {
    clipPath: "polygon(0 0, 100% 0, 100% 100%, 0 100%)",
    duration: 1,
    ease: "power3.out"
})

// Subtitle fade
n.a.fromTo(studioSubtitle, {
    autoAlpha: 0,
    y: 20
}, {
    autoAlpha: 1,
    y: 0,
    duration: 0.8,
    delay: 0.5,
    ease: "power2.out"
})
```

**Animation Details:**
- Bottom-to-top clip path reveal
- Subtitle follows with delay
- Power3 for stronger ease on title

---

### 3. TEAM MEMBER CARDS

```javascript
// Card entrance
n.a.fromTo(teamCards, {
    autoAlpha: 0,
    y: 60,
    rotation: 3
}, {
    autoAlpha: 1,
    y: 0,
    rotation: 0,
    stagger: {
        amount: 1,
        grid: [2, 3],  // 2 rows, 3 columns
        from: "start"
    },
    duration: 0.8,
    ease: "power2.out",
    scrollTrigger: {
        trigger: teamSection,
        start: "top 70%"
    }
})

// Card hover - image zoom
n.a.to(teamImage, {
    scale: 1.1,
    duration: 0.6,
    ease: "power2.out"
})

// Card hover - overlay reveal
n.a.to(teamOverlay, {
    autoAlpha: 1,
    duration: 0.4,
    ease: "power1.out"
})
```

**Animation Details:**
- Grid-based stagger (respects layout)
- Slight rotation on entrance (3deg)
- Hover: image zoom + overlay reveal

---

### 4. PROCESS/HOW WE WORK STEPS

```javascript
// Step container reveal
n.a.fromTo(processSteps, {
    autoAlpha: 0,
    x: -100
}, {
    autoAlpha: 1,
    x: 0,
    stagger: 0.3,
    duration: 0.8,
    ease: "power2.out",
    scrollTrigger: {
        trigger: processSection,
        start: "top 65%"
    }
})

// Step number count-up animation
n.a.to(stepNumber, {
    innerText: targetNumber,
    duration: 1,
    snap: { innerText: 1 },  // Snap to whole numbers
    ease: "power1.out"
})
```

**Animation Details:**
- Slide in from left
- Longer stagger (300ms) for readability
- Number count-up effect with snap

---

### 5. AWARDS/RECOGNITION SECTION

```javascript
// Award badges float in
n.a.fromTo(awardBadges, {
    autoAlpha: 0,
    y: 50,
    scale: 0.8
}, {
    autoAlpha: 1,
    y: 0,
    scale: 1,
    stagger: {
        each: 0.15,
        from: "center"
    },
    duration: 0.8,
    ease: "back.out(1.2)"
})
```

**Animation Details:**
- From center stagger pattern
- Back ease for subtle bounce
- Scale + fade + Y-movement combination

═══════════════════════════════════════════════════════════════════════════════

## FILE: a4c5813.js (82KB)
### PRIMARY: Work/Project List Page

---

### 1. PROJECT LIST ITEM ANIMATIONS

```javascript
// Project row entrance
n.a.fromTo(projectRows, {
    autoAlpha: 0,
    x: -50
}, {
    autoAlpha: 1,
    x: 0,
    stagger: 0.08,
    duration: 0.6,
    ease: "power2.out",
    scrollTrigger: {
        trigger: projectList,
        start: "top 80%"
    }
})

// Project thumbnail reveal on hover
n.a.fromTo(projectThumbnail, {
    clipPath: "inset(0 100% 0 0)"
}, {
    clipPath: "inset(0 0% 0 0)",
    duration: 0.6,
    ease: "power2.inOut"
})
```

**Animation Details:**
- List rows slide in from left
- Fast stagger (80ms)
- Thumbnail wipes in left-to-right on hover

---

### 2. FILTER/CATEGORY TABS

```javascript
// Tab switch animation
n.a.to(activeTab, {
    x: tabPosition,
    width: tabWidth,
    duration: 0.4,
    ease: "power2.inOut"
})

// Content fade out/in
n.a.timeline()
    .to(currentContent, {
        autoAlpha: 0,
        y: -20,
        duration: 0.2,
        ease: "power1.in"
    })
    .to(newContent, {
        autoAlpha: 1,
        y: 0,
        duration: 0.3,
        ease: "power2.out"
    }, 0.1)
```

**Animation Details:**
- Active indicator slides to new position
- Content crossfade with slight Y-movement
- Timeline for choreography

---

### 3. PROJECT YEAR LABELS

```javascript
// Year label sticky reveal
n.a.fromTo(yearLabel, {
    autoAlpha: 0,
    scale: 0.9
}, {
    autoAlpha: 1,
    scale: 1,
    duration: 0.4,
    ease: "back.out(1.5)",
    scrollTrigger: {
        trigger: yearSection,
        start: "top 100px",
        toggleActions: "play none none reverse"
    }
})
```

**Animation Details:**
- Year labels appear as you scroll to new year
- Back ease for subtle pop
- Reverse on scroll up

═══════════════════════════════════════════════════════════════════════════════

## FILE: 5353853.js (15KB)
### PRIMARY: Rich Text & Content Components

---

### 1. RICH TEXT PARAGRAPH REVEALS

```javascript
// Paragraph fade-in sequence
n.a.fromTo(richTextParagraphs, {
    autoAlpha: 0,
    y: 30
}, {
    autoAlpha: 1,
    y: 0,
    stagger: 0.2,
    duration: 0.8,
    ease: "power2.out",
    scrollTrigger: {
        trigger: richTextContainer,
        start: "top 70%"
    }
})
```

**Animation Details:**
- Standard paragraph reveal pattern
- 200ms stagger between paragraphs
- Used across multiple content sections

---

### 2. BLOCKQUOTE ANIMATIONS

```javascript
// Quote slide in with line
n.a.fromTo(blockquoteLine, {
    scaleY: 0,
    transformOrigin: "top"
}, {
    scaleY: 1,
    duration: 0.6,
    ease: "power2.out"
})

n.a.fromTo(blockquoteText, {
    autoAlpha: 0,
    x: -20
}, {
    autoAlpha: 1,
    x: 0,
    duration: 0.8,
    delay: 0.2,
    ease: "power2.out"
})
```

**Animation Details:**
- Vertical line grows from top
- Text slides in after line appears
- Common pattern for emphasized content

═══════════════════════════════════════════════════════════════════════════════

## MASTER ANIMATION PATTERNS COMPILATION

### Common Animation Durations
```javascript
0.1s  - Instant fade (menu middle line)
0.2s  - Quick transitions (video thumbnail swap)
0.3s  - Fast interactions (overlays, small elements)
0.4s  - Standard interactions (tab switches, hover effects)
0.6s  - Medium animations (menu open, clip paths)
0.8s  - Content reveals (cards, sections)
1.0s  - Major animations (titles, hero sections)
1.2s  - Slow emphasis (hero images, major reveals)
```

### Common Stagger Patterns
```javascript
stagger: 0.05   // Very fast - footer links
stagger: 0.08   // Fast - list items, navigation
stagger: 0.1    // Standard - title lines
stagger: 0.12   // Slightly slower - hero lines
stagger: 0.15   // Medium - badges, awards
stagger: 0.2    // Slow - paragraphs
stagger: 0.3    // Very slow - process steps
```

### Common Easing Functions
```javascript
// Custom curves
"M0,0 C0,0.202 0.204,1 1,1"      // Gentle (most common)
"M0,0 C0.496,0.004 0,1 1,1"       // Strong

// GSAP built-in
"power1.out"    // Gentle deceleration
"power2.out"    // Medium deceleration (most common)
"power3.out"    // Strong deceleration
"power2.inOut"  // Smooth both ends
"back.out(1.7)" // Overshoot bounce
"back.out(2)"   // Stronger bounce
"expo.out"      // Exponential deceleration
"none"          // Linear (scroll animations)
```

### ScrollTrigger Patterns
```javascript
// Standard reveal
scrollTrigger: {
    trigger: element,
    start: "top 70%",
    toggleActions: "play none none reverse"
}

// Parallax
scrollTrigger: {
    trigger: section,
    start: "top bottom",
    end: "bottom top",
    scrub: 1
}

// Horizontal scroll
scrollTrigger: {
    trigger: section,
    start: "top top",
    end: "+=dynamicValue",
    scrub: 1,
    pin: true,
    anticipatePin: 1
}
```

### Transform Combinations
```javascript
// Entrance pattern (most common)
FROM: { autoAlpha: 0, y: 30-100, scale: 0.9-0.95, rotation: 3-7 }
TO:   { autoAlpha: 1, y: 0, scale: 1, rotation: 0 }

// Hover pattern
TO: { scale: 1.02-1.1, y: -2 to -5 }

// Exit pattern  
TO: { autoAlpha: 0, y: -20 to -50, scale: 0.95 }
```

═══════════════════════════════════════════════════════════════════════════════

## IMPLEMENTATION CHECKLIST

To recreate Exo Ape animations, you need:

### 1. Core Dependencies
- GSAP 3.x (gsap.min.js)
- ScrollTrigger plugin
- CustomEase plugin (for custom curves)

### 2. Page Transition System
- Nuxt page transition hooks or custom router transitions
- Clip path polygon animations
- Loading state management
- Mobile vs desktop timing

### 3. Scroll Animation System
- ScrollTrigger for all scroll-based reveals
- RAF (RequestAnimationFrame) for performance
- Intersection Observer for viewport detection
- Scrub values for smooth parallax

### 4. Component Animations
- Title split animation mixin (reusable)
- Image lazy load animations
- Video thumbnail hover swaps
- Navigation menu system
- Loader/preloader component

### 5. Performance Optimizations
- `will-change: transform` on animated elements
- `clearProps: "all"` after animations
- Hardware acceleration (`translateZ(0)`)
- Debounced scroll handlers
- Proper cleanup in `beforeDestroy`

### 6. CSS Custom Properties
- Color system with opacity variants
- Typography scales (vw-based)
- Consistent transition timings
- Transform origins

═══════════════════════════════════════════════════════════════════════════════

END OF PART 2

Total files covered: 12/12
- Part 1: 0efa5ea.js, e36d691.js, 7bc4024.js, 67eac05.js
- Part 2: 9fcf850.js, d5d162b.js, e3cea04.js, a4c5813.js, 5353853.js, 1475246.js, b6072a7.js, 7aefc33.js

═══════════════════════════════════════════════════════════════════════════════
