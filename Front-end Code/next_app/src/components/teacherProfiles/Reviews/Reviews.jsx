
"use client"
import React, { useState } from 'react';
import styles from './Reviews.module.css';

const Reviews = ({ reviews }) => {
    const reviewsPerPage = 5;
    const [currentPage, setCurrentPage] = useState(1);

    // Total Page Number
    const numberOfPages = Math.ceil(reviews.length / reviewsPerPage);

    // Get current page
    const currentReviews = reviews.slice(
        (currentPage - 1) * reviewsPerPage,
        currentPage * reviewsPerPage
    );

    // Bottom Last Page
    const handlePrevious = () => {
        setCurrentPage((prev) => (prev > 1 ? prev - 1 : prev));
    };

    // Next Page
    const handleNext = () => {
        setCurrentPage((prev) => (prev < numberOfPages ? prev + 1 : prev));
    };

    // jump to the page
    const handleJump = (e) => {
        const pageNumber = parseInt(e.target.value, 10);
        if (pageNumber > 0 && pageNumber <= numberOfPages) {
            setCurrentPage(pageNumber);
        }
    };

    return (
        <div className={styles.container}>
            <h2>Reviews</h2>
            <ul className={styles.reviewList}>
                {currentReviews.map((review, index) => (
                    <li key={index} className={styles.reviewItem}>
                        <div className={styles.reviewerInfo}>
                            <div className={styles.avatar}></div>
                            <p className={styles.name}>{review.name}</p>
                        </div>
                        <div
                            className={styles.rating}>{'★'.repeat(review.rating)}
                        </div>
                        <p className={styles.content}>{review.content}</p>
                    </li>
                ))}
            </ul>
            <div className={styles.pagination}>
                <button onClick={handlePrevious} disabled={currentPage === 1}>
                    Last
                </button>
                <span>
          Page {currentPage} of {numberOfPages}
        </span>
                <button onClick={handleNext} disabled={currentPage === numberOfPages}>
                    Next
                </button>
                <input
                    type="number"
                    placeholder="Jump to"
                    onBlur={handleJump}
                    onKeyPress={(e) => e.key === 'Enter' && handleJump(e)}
                />
            </div>
        </div>
    );
};

export default Reviews;
