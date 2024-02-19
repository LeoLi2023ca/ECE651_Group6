"use client"

import React from "react";
import styles from "./scBtn.module.css";

const ScBtn = () => {
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  };

  // Note: We're using a button element now instead of Link
  return (
    <button onClick={scrollToTop} className={styles.container}>
      Back to Top
    </button>
  );
};

export default ScBtn;


// import React from "react";
// import Link from "next/link";
// import styles from "./scLink.module.css";

// const ScLink = () => {
//   const scrollToTop = () => {
//     window.scrollTo({
//       top: 0,
//       behavior: 'smooth'
//     });
//   };

//   return (
//     <Link href="/" className={styles.container}
//       onClick={scrollToTop}>
//       Back to Top
//     </Link>
//   );
// };

// export default ScLink;
