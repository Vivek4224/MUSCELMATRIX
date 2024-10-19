// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
  // Animate the profile container to fade in and slide up
  gsap.to(".profile-container", {
    opacity: 1,
    y: -20,
    duration: 1,
    ease: "power2.out",
  });

  // Animate each info item on scroll
  const infoItems = document.querySelectorAll(".info-item");
  infoItems.forEach((item, index) => {
    gsap.from(item, {
      opacity: 0,
      y: 20,
      duration: 0.5,
      delay: index * 0.2,
      ease: "power2.out",
      scrollTrigger: {
        trigger: item,
        start: "top 80%",
        toggleActions: "play none none reverse",
      },
    });
  });
});
