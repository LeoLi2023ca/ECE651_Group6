"use client";

import { useState } from "react";
import styles from "./links.module.css";
import NavLink from "./navLink/navLink";
import Image from "next/image";
import TutorAvatar from "@/components/tutorAvatar/tutorAvatar";
import StudentAvatar from "@/components/studentAvatar/studentAvatar";

const links = [
  {
    title: "Chat",
    path: "/",
  },
  
];

const Links = () => {
  const [open, setOpen] = useState(false)

  //TEMPORARY
  const session = true
  const data = localStorage.getItem('isTutor');
  const isTutor = data?true:false
  return (
    <div className={styles.container}>
      <div className={styles.links}>
        {links.map((link => (
          <NavLink item={link} key={link.title} />
        )))}
        {session ? (
          <>
            {isTutor ? (
              <>
                {/* <NavLink item={{ title: "Schedule", path: "/schedule" }} /> */}
                <NavLink item={{ title: "Post", path: "/tutor-post" }} />
                <NavLink item={{ title: "Find students", path: "/find-students" }} />
                <NavLink item={{ title: "Match students", path: "/match-me-with-students" }} />
                {/* <NavLink item={{ title: "Profile", path: "/tutor-profile" }} /> */}
                <TutorAvatar />
              </>)
              : (
                <>
                  {/* <NavLink item={{ title: "Schedule", path: "/schedule" }} /> */}
                  <NavLink item={{ title: "Post", path: "/student-post" }} />
                  <NavLink item={{ title: "Find tutors", path: "/find-tutors" }} />
                  <NavLink item={{ title: "Match tutors", path: "/match-me-with-tutors" }} />
                  {/* <NavLink item={{ title: "Profile", path: "/student-profile" }} /> */}
                  <StudentAvatar />
                </>)}
            {/* <button className={styles.logout}>Log out</button> */}
            
          </>
        ) : (
          <>
            <NavLink item={{ title: "Log in", path: "/login" }} />
            <NavLink item={{ title: "Register", path: "/register" }} />
          </>
        )}
      </div>
      <Image
        className={styles.menuButton}
        src="/menu.png"
        alt=""
        width={30}
        height={30}
        onClick={() => setOpen((prev) => !prev)}
      />
      {open && <div className={styles.mobileLinks}>
        {links.map((link) => (
          <NavLink item={link} key={styles.title} />
        ))}
      </div>
      }
    </div>
  );
};

export default Links;