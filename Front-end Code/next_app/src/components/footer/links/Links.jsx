"use client";

import { useState } from "react";
import styles from "./links.module.css";
import NavLink from "./navLink/navLink";
// import Image from "next/image";

const links = [
  {
    title: "About us",
    path: "/about-us",
  },
  {
    title: "Contact",
    path: "/contact",
  },

];

const Links = () => {
  const [open, setOpen] = useState(false)

  // //TEMPORARY
  // const session = false
  // const isAdmin = false

  return (
    <div className={styles.container}>
      <div className={styles.links}>
        {links.map((link => (
          <NavLink item={link} key={link.title} />
        )))}
        {/* {session ? (
          <>
            {isAdmin && <NavLink item={{ title: "Admin", path: "/admin" }} />}
            <button className={styles.logout}>Log out</button>
          </>
        ) : (
          <>
            <NavLink item={{ title: "Log in", path: "/login" }} />
            <NavLink item={{ title: "Register", path: "/register" }} />
          </>
        )} */}
      </div>
      {/* {open && <div className={styles.mobileLinks}>
        {links.map((link) => (
          <NavLink item={link} key={styles.title} />
        ))}
      </div>
      } */}
    </div>
  );
};

export default Links;