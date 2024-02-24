import React from 'react';
import styles from './postCard.module.css';

const PostCard = ({ post, onClick }) => {
    return (
        <div className={styles.card} onClick={() => onClick(post)}>
            <div className={styles.postId}>ID: {post.post_id}</div>
            {/*<div className={styles.name}>Name: {post.name}</div>*/}
            <div className={styles.subject}>Subjects: {post.subjects}</div>
            <p className={styles.title}>{post.title}</p>
            <div className={styles.dateAndAvailableTime}>
                <span className={styles.date}>Date: {post.date}</span>
                <span className={styles.availableTime}>Available time: {post.available_time}</span>
            </div>
            <p className={styles.msg}>{post.msg}</p> {/* Assuming msg as summary */}
             {/*<div className={styles.status}>{post.status}</div> */}
            <div className={styles.salary}>Salary: <span className={styles.salaryAmount}>{post.salary}</span></div>
        </div>
    );
};

export default PostCard;
