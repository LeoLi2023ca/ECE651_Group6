import React from 'react';
import styles from './titleBox.module.css'; // 确保路径正确

const TitleBox = ({post}) => {
    return (
        <div className={styles.titleBox}>
            <div className={styles.infoItem}>
                <span className={styles.postId}>Post ID: {post.post_id}</span>
            </div>
            <div className={styles.infoItem}>
                <span className={styles.studentName}>Student Name: {post.studentName}</span>
            </div>
            <div className={styles.infoItem}>
                <span className={styles.studentID}>Student ID: {post.studentID}</span>
            </div>
        </div>
    );
};

export default TitleBox;
