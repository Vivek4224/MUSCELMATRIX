// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
  // Animate the container to fade in and slide up
  gsap.to(".tac_container", {
    // Update the selector to match the HTML
    opacity: 1,
    y: -20,
    duration: 1,
    ease: "power2.out",
  });

  // Animate each section on scroll
  const sections = document.querySelectorAll(".tac_content h2, .tac_content p"); // Update the selector to match the HTML
  sections.forEach((section, index) => {
    gsap.from(section, {
      opacity: 0,
      y: 20,
      duration: 0.5,
      delay: index * 0.2,
      ease: "power2.out",
      scrollTrigger: {
        trigger: section,
        start: "top 80%",
        toggleActions: "play none none reverse",
      },
    });
  });
});
