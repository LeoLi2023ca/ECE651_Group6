"use client"

import StudentPostTable from "@/components/studentPostTable/studentPostTable";
import StudentSearchBox from "@/components/studentSearchBox/studentSearchBox";
import styles from "./findStudents.module.css";
import { getPosts } from "@/lib/data";
import React, { useState, useEffect } from 'react';

const FindStudentsPage = () => {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        setPosts(getPosts());
    }, []);

    return (
        <div className={styles.container}>
            <StudentSearchBox />
            <StudentPostTable data={posts} />
        </div>
    );
};

export default FindStudentsPage;


// return (

//     <div className={styles.container}>
//         {posts.map((post) => (
//             <div className={styles.post} key={post.id}>
//                 <PostTable post={post} />
//             </div>
//         ))}
//     </div>
// )






