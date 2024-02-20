"use client"
// components/Package.jsx
import React, { useState } from 'react';
import styles from './TutorPackages.module.css';

const Package = ({ tutorName, rating, trialPrice, packages }) => {
    const [duration, setDuration] = useState(25); // The default display is a 25-minute lesson

    const renderRating = (rating) => {
        const fullStars = Math.floor(rating);
        const halfStar = rating % 1 >= 0.5 ? 1 : 0;
        const emptyStars = 5 - fullStars - halfStar;
        return (
            <>
                {'★'.repeat(fullStars)}
                {halfStar ? '☆' : ''}
                {''.repeat(emptyStars)}
            </>
        );
    };

    return (
        <div className={styles.packageContainer}>

            <div className={styles.tutorHeader}>
                <h2>{tutorName}</h2>
                <div className={styles.rating}>{renderRating(rating)}</div>
            </div>

            <div className={styles.trial}>
                <div className={styles.trialDetails}>
                    <span className={styles.price}>{`CA$${trialPrice}`}</span>
                    <span className={styles.trialLabel}>25min Trial</span>
                </div>
                <button className={styles.bookButton}>Contact</button>
            </div>


            <div className={styles.durationSwitch}>
                <button
                    className={`${styles.durationButton} ${duration === 25 ? styles.active : ''}`}
                    onClick={() => setDuration(25)}
                >
                    25 mins
                </button>
                <button
                    className={`${styles.durationButton} ${duration === 50 ? styles.active : ''}`}
                    onClick={() => setDuration(50)}
                >
                    50 mins
                </button>
            </div>

            <div className={styles.packagesList}>
                {packages
                    .filter(pkg => pkg.duration === duration)
                    .map((pkg, index) => (
                        <div className={styles.packageItem} key={index}>
                            <div className={styles.packagePriceDetails}>
                                <div className={styles.packagePrice}>{`CA$${pkg.price}`}</div>
                                <div
                                    className={styles.sessionDetails}>{`${pkg.sessions} lesson `}</div>
                            </div>
                            <div className={styles.bookingSection}>
                                {pkg.discount && <div className={styles.discount}>{pkg.discount}</div>}
                                <button className={styles.bookButton}>Contact</button>
                            </div>
                        </div>
                    ))}
            </div>

        </div>
    );
};

export default Package;
