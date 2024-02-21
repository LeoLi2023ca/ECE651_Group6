import React, { useState } from 'react';
import styles from './postModal.module.css';
import InfoBox from "@/components/postComponents/InfoBox";
import EditInfoBox from "@/components/postComponents/EditInfoBox";
import TitleBox from "@/components/postComponents/TitleBox";

const PostModal = ({ post, onClose }) => {
    const [isEditing, setIsEditing] = useState(false);

    // If there is no post, return null
    if (!post) return null;

    // Edit mode switch
    const handleEdit = () => {
        setIsEditing(!isEditing);
    };

    return (
        <div className={styles.modal}>
            <div className={styles.modalContent}>
                <div className={styles.header}>
                    <button onClick={handleEdit} className={styles.editButton}>Edit</button>
                    <button onClick={onClose} className={styles.closeButton}>Close</button>
                </div>
                <div className={styles.infoBox}>
                    <TitleBox post={post} />
                </div>
                {/*  Determines whether to render the InfoBox or EditInfoBox based on the isEditing state. */}
                {isEditing ? <EditInfoBox post={post} /> : <InfoBox post={post} />}
            </div>
        </div>
    );
};

export default PostModal;
