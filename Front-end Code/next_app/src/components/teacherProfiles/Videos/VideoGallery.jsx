// components/VideoGallery.jsx
"use client"
// components/VideoGallery.jsx
import React, { useState } from 'react';
import styles from './VideoGallery.module.css';

const VideoGallery = ({ videos }) => {
    const [selectedVideoID, setSelectedVideoID] = useState(null);

    const openModal = (videoID) => {
        setSelectedVideoID(videoID);
    };

    const closeModal = () => {
        setSelectedVideoID(null);
    };

    const extractYouTubeID = (url) => {
        const regExp = /^.*(youtu\.be\/|v\/|e\/|u\/\w+\/|embed\/|v=)([^#\\&\\?]*).*/;
        const match = url.match(regExp);
        return (match && match[2].length === 11) ? match[2] : null;
    };

    const getYouTubeThumbnail = (videoID) => {
        return `https://img.youtube.com/vi/${videoID}/hqdefault.jpg`;
    };

    return (
        <>
            <div className={styles.gallery}>
                {videos.map((video, index) => {
                    const videoID = extractYouTubeID(video.url);
                    return (
                        <div key={index} className={styles.videoItem}>
                            <button onClick={() => openModal(videoID)} className={styles.thumbnailButton}>
                                <img src={getYouTubeThumbnail(videoID)} alt={`Play ${video.title}`} className={styles.thumbnail} />
                                <div className={styles.playIcon}>▶</div>
                            </button>
                            <p className={styles.title}>{video.title}</p>
                        </div>
                    );
                })}
            </div>

            {selectedVideoID && (
                <div className={styles.modal} onClick={closeModal}>
                    <div className={styles.modalContent} onClick={(e) => e.stopPropagation()}>
                        <iframe
                            src={`https://www.youtube.com/embed/${selectedVideoID}?autoplay=1&rel=0`}
                            title="YouTube video player"
                            frameBorder="0"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowFullScreen
                            className={styles.iframe}
                        ></iframe>
                        <button onClick={closeModal} className={styles.closeModalButton}>✕</button>
                    </div>
                </div>
            )}
        </>
    );
};

export default VideoGallery;
