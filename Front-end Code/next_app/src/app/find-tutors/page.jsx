"use client"

import TutorPostTable from "@/components/tutorPostTable/tutorPostTable";
import TutorSearchBox from "@/components/tutorSearchBox/tutorSearchBox";
import styles from "./findTutors.module.css";
import { getPosts } from "@/lib/data";
import React, { useState, useEffect } from 'react';

const FindTutorsPage = () => {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        setPosts(getPosts());
    }, []);

    return (
        <div className={styles.container}>
            <TutorSearchBox />
            <TutorPostTable data={posts} />
        </div>
    );
};

export default FindTutorsPage;








