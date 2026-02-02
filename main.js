document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.getElementById('navbar');
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    // Sticky Navbar
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Mobile Menu Toggle
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');

            // Hamburger Animation (optional, can be added in CSS)
            mobileMenuBtn.classList.toggle('open');
        });
    }

    // Smooth Scrolling for nav links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 80,
                    behavior: 'smooth'
                });
                // Close mobile menu if open
                if (window.innerWidth <= 1024) {
                    navLinks.classList.remove('active');
                    mobileMenuBtn.classList.remove('open');
                }
            }
        });
    });

    // Animation on Scroll using Intersection Observer
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    // Select elements to animate
    // We now select anything that ALREADY has an animation class, plus specific elements we want to auto-animate
    const animateElements = document.querySelectorAll(`
        .reveal, .reveal-up, .reveal-left, .reveal-right, .reveal-scale, .fade-up,
        h1, h2, h3, h4, 
        .btn-connect-now, .btn-know-more, .cta-pill-btn,
        .about-image-card, .tab-image, .product-card,
        .award-badge-container
    `);

    animateElements.forEach((el) => {
        // Only add default 'reveal' if it doesn't already have an animation class
        if (!el.classList.contains('reveal') &&
            !el.classList.contains('reveal-up') &&
            !el.classList.contains('reveal-left') &&
            !el.classList.contains('reveal-right') &&
            !el.classList.contains('reveal-scale') &&
            !el.classList.contains('fade-up')) {

            if (el.classList.contains('product-card') || el.classList.contains('tab-image') || el.classList.contains('about-image-card')) {
                el.classList.add('reveal-scale');
            } else {
                el.classList.add('reveal');
            }
        }

        observer.observe(el);
    });

    // FAQ Toggle
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');

        // Hide answers by default
        answer.style.display = 'none';

        question.addEventListener('click', () => {
            const isOpen = answer.style.display === 'block';

            // Close all other answers
            document.querySelectorAll('.faq-answer').forEach(ans => ans.style.display = 'none');
            document.querySelectorAll('.faq-question i').forEach(icon => icon.style.transform = 'rotate(0deg)');

            if (!isOpen) {
                answer.style.display = 'block';
                question.querySelector('i').style.transform = 'rotate(180deg)';
            }
        });
    });

    // Dropdown Toggle for Mobile
    const dropdownToggles = document.querySelectorAll('.has-dropdown > a');
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            if (window.innerWidth <= 1024) {
                e.preventDefault();
                const menu = toggle.nextElementSibling;
                if (menu) {
                    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
                }
            }
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (window.innerWidth <= 1024) {
            if (navLinks.classList.contains('active') &&
                !navLinks.contains(e.target) &&
                !mobileMenuBtn.contains(e.target)) {
                navLinks.classList.remove('active');
                mobileMenuBtn.classList.remove('open');
            }
        }
    });
    // Why Choose Section Tabs
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons and contents
            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));

            // Add active class to clicked button
            btn.classList.add('active');

            // Show corresponding tab content
            const tabId = btn.getAttribute('data-tab');
            const targetContent = document.getElementById(tabId);
            if (targetContent) {
                targetContent.classList.add('active');
            }
        });
    });

    // Number Counter Animation
    const statsSection = document.querySelector('.stats-section');
    const statNumbers = document.querySelectorAll('.stat-number');
    let started = false; // Function started ? No

    if (statsSection) {
        const statsObserver = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting && !started) {
                statNumbers.forEach(num => startCount(num));
                started = true;
            }
        });

        statsObserver.observe(statsSection);
    }

    function startCount(el) {
        const target = parseInt(el.dataset.target);
        let current = 0;

        // Normalize duration to ~2000ms for all numbers
        const duration = 2000;
        let increment = 1;
        let intervalTime = 20;

        // For small numbers (like 30), adjust interval to be slower
        if (target < 100) {
            intervalTime = Math.floor(duration / target);
        } else {
            // For large numbers, adjust increment to fit in 2000ms with 20ms interval
            // Total steps = 2000 / 20 = 100 steps
            increment = Math.ceil(target / 100);
        }

        const count = setInterval(() => {
            current += increment;

            if (current >= target) {
                current = target;
                clearInterval(count);
            }

            // Special formatting for 10k
            if (target === 10000 && current === target) {
                el.innerHTML = '10k<span class="plus">+</span>';
            } else {
                el.innerHTML = current + '<span class="plus">+</span>';
            }
        }, intervalTime);
    }

    // Interactive Door Color Swatches
    const swatches = document.querySelectorAll('.color-swatch');
    const doorImg = document.getElementById('interactive-door');
    const doorLabel = document.getElementById('door-label');

    if (swatches.length && doorImg) {
        swatches.forEach(swatch => {
            swatch.addEventListener('click', () => {
                // Update Active State
                swatches.forEach(s => {
                    s.style.border = '2px solid transparent';
                    s.style.boxShadow = 'none';
                    if (s.title === "White") s.style.border = '1px solid #ccc';
                });

                // Add active style to clicked swatch
                swatch.style.border = '2px solid #fff';
                swatch.style.boxShadow = `0 0 0 2px ${swatch.style.backgroundColor}`;

                // Handle Image Swap & Filter
                const imgSource = swatch.getAttribute('data-img');
                const filterVal = swatch.getAttribute('data-filter');

                // 1. Swap Image if provided
                if (imgSource && doorImg.getAttribute('src') !== imgSource) {
                    // Simple fade out/in effect could be added here, but direct swap is faster
                    doorImg.src = imgSource;
                }

                // 2. Apply Filter (or reset)
                doorImg.style.transition = 'filter 0.5s ease';
                if (filterVal) {
                    doorImg.style.filter = filterVal;
                } else {
                    doorImg.style.filter = 'none';
                }

                // Update Label
                if (doorLabel) {
                    doorLabel.innerText = swatch.getAttribute('data-name');
                    doorLabel.style.opacity = 0;
                    setTimeout(() => {
                        doorLabel.style.opacity = 1;
                    }, 50);
                }
            });
        });
    }

    // Latest Offerings Filter
    const filterBtns = document.querySelectorAll('.filter-btn');
    const offeringCards = document.querySelectorAll('.offering-card');

    if (filterBtns.length) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Update active button
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filterValue = btn.getAttribute('data-filter');

                offeringCards.forEach(card => {
                    const category = card.getAttribute('data-category');

                    if (filterValue === 'all' || filterValue === category) {
                        card.style.display = 'flex';
                        // Small animation to show it's refreshing
                        card.style.opacity = '0';
                        card.style.transform = 'scale(0.9)';
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'scale(1)';
                        }, 50);
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    // Transformation Slider Logic
    const sliderRange = document.getElementById('slider-range');
    const beforeLayer = document.querySelector('.before-layer');
    const sliderHandle = document.querySelector('.slider-handle');
    const compViewer = document.getElementById('comp-viewer');
    const beforeOverlay = document.querySelector('.before-overlay');

    if (sliderRange && beforeLayer && sliderHandle && compViewer && beforeOverlay) {
        function updateSlider() {
            const val = sliderRange.value;
            beforeLayer.style.width = `${val}%`;
            sliderHandle.style.left = `${val}%`;

            // Magic Trick: Keep the inner image full width of the CONTAINER,
            // so it looks like we are 'revealing' it, not resizing it.
            // We need to calculate width relative to the percentage.
            // If container is 1000px, and val is 50%, beforeLayer is 500px.
            // beforeOverlay needs to be 1000px wide.
            // So width = 100% * (100/val)

            if (val > 0) {
                beforeOverlay.style.width = `${100 * (100 / val)}%`;
            } else {
                beforeOverlay.style.width = '0'; // Hide
            }
        }

        sliderRange.addEventListener('input', updateSlider);
        sliderRange.addEventListener('change', updateSlider);

        // Initial call
        updateSlider();

        // Handle Resize to keep images aligned if using pixel logic (here we use %),
        // but let's ensure object-fit works.
    }

    // Door Collections Filter
    const doorFilterTabs = document.querySelectorAll('.filter-tab');
    const doorItems = document.querySelectorAll('.door-item');

    if (doorFilterTabs.length) {
        doorFilterTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                // Update active tab
                doorFilterTabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');

                const filterValue = tab.getAttribute('data-filter');

                doorItems.forEach(item => {
                    const category = item.getAttribute('data-category');

                    if (filterValue === 'all' || filterValue === category) {
                        item.classList.remove('hidden');
                        // Add fade-in animation
                        item.style.opacity = '0';
                        item.style.transform = 'scale(0.95)';
                        setTimeout(() => {
                            item.style.opacity = '1';
                            item.style.transform = 'scale(1)';
                        }, 50);
                    } else {
                        item.classList.add('hidden');
                    }
                });
            });
        });
    }

    // Aluminium Section Tabs
    const aluTabs = document.querySelectorAll('.alu-tab');
    const aluContents = document.querySelectorAll('.alu-content');

    if (aluTabs.length) {
        aluTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                // Remove active class from all tabs and contents
                aluTabs.forEach(t => t.classList.remove('active'));
                aluContents.forEach(c => c.classList.remove('active'));

                // Add active class to clicked tab
                tab.classList.add('active');

                // Show corresponding content
                const tabId = tab.getAttribute('data-tab');
                const targetContent = document.getElementById(tabId);
                if (targetContent) {
                    targetContent.classList.add('active');
                }
            });
        });
    }

    // Customise Section Accordion
    const accordionItems = document.querySelectorAll('.accordion-item');
    accordionItems.forEach(item => {
        const header = item.querySelector('.accordion-header');
        header.addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            // Close all items
            accordionItems.forEach(i => {
                i.classList.remove('active');
                i.querySelector('i').classList.replace('fa-minus', 'fa-plus');
            });

            // If the clicked item wasn't active, open it
            if (!isActive) {
                item.classList.add('active');
                header.querySelector('i').classList.replace('fa-plus', 'fa-minus');
            }
        });
    });
    // --- WHATSAPP FORM HANDLING ---
    const whatsappSubmitBtn = document.getElementById('whatsappSubmitBtn');
    if (whatsappSubmitBtn) {
        whatsappSubmitBtn.addEventListener('click', function (e) {
            e.preventDefault();

            const name = document.getElementById('userName').value;
            const phone = document.getElementById('userPhone').value;
            const requirements = document.getElementById('userRequirements').value;

            if (!name || !phone || !requirements) {
                alert("Please fill in all details before sending.");
                return;
            }

            const phoneNumber = "919171994284"; // Your WhatsApp number
            const message = `Hello Naresh UPVC, %0A%0A*New Inquiry from Website*%0A*Name:* ${name}%0A*Phone:* ${phone}%0A*Requirements:* ${requirements}`;

            window.open(`https://wa.me/${phoneNumber}?text=${message}`, '_blank');
        });
    }

    // --- GLOBAL WHATSAPP CONNECT BUTTONS ---
    // Ensuring all buttons with WhatsApp links have a default friendly message
    const waButtons = document.querySelectorAll('a[href*="wa.me"]');
    waButtons.forEach(btn => {
        const currentHref = btn.getAttribute('href');
        if (!currentHref.includes('text=')) {
            const defaultMsg = encodeURIComponent("Hello Naresh UPVC, I'm interested in your services and would like to know more.");
            btn.setAttribute('href', `${currentHref}?text=${defaultMsg}`);
        }
    });

});
