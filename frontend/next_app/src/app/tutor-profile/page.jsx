"use client"
// pages/tutor-profile.js
import React, { useState } from 'react';
import styles from "./tutorProfile.module.css";
import TutorProfileHeader from '@/components/teacherProfiles/Header/TutorProfileHeader';
import TutorInfo from '@/components/teacherProfiles/Intros/TutorInfo';
import TutorIntroduction from '@/components/teacherProfiles/Intros/TutorIntroduction';
import LessonsInformation from '@/components/teacherProfiles/Intros/LessonsInformation';
import VideoGallery from '@/components/teacherProfiles/Videos/VideoGallery';
import TutorPackages from "@/components/teacherProfiles/Package/TutorPackages";
import Reviews from '@/components/teacherProfiles/Reviews/Reviews';
import Resume from '@/components/teacherProfiles/Intros/TutorResume';
import FAQ from '@/components/teacherProfiles/FAQ/FAQ';
import EditProfile from "@/components/teacherProfiles/Edit/EditProfile";



const TutorProfilePage = () => {

    const [tutorProfileData, setTutorProfileData] = useState({
        ID: "12343",
        name: "John Doe",
        avatarUrl: "https://bpic.51yuansu.com/pic3/cover/04/06/00/65901191b4b91_800.jpg?x-oss-process=image/sharpen,100",
        subject : "Physics",
        tagline : "Dedicated and experienced Physics tutor ready to help you succeed!",
        highestDegree: "Master",
        graduatedFrom: "University of Waterloo",
        birthYear: 1980,
        certifications: ['TESOL', 'CELTA'],
        teachingDuration: 1200,
        rating: 4.3,
        trailPrice: 5.99,
        package:[
            { duration: 25, price: '18.69', sessions: 1 },
            { duration: 25, price: '17.76', sessions: 10, discount: '5% off' },
            { duration: 50, price: '17.76', sessions: 10, discount: '5% off' },
        ],
        introText: "Long introduction text goes here...",
        lessonInfoText: "Detailed lessons information goes here...",
        videos: [
            {
                url: 'https://www.youtube.com/watch?v=k-T8L-WIGXQ', //YouTube video only
                title: 'Self-Intro Video',
            },
            {
                url: 'https://www.youtube.com/watch?v=k-T8L-WIGXQ', //YouTube video only
                title: 'Self-Intro Video',
            },
            {
                url: 'https://www.youtube.com/watch?v=k-T8L-WIGXQ', //YouTube video only
                title: 'Self-Intro Video',
            }
        ],
        reviews: [
            {name: 'Reviewer Name', content: 'Review content'},
            {name: 'Reviewer Name', content: 'Review content'},
            {name: 'Reviewer Name', content: 'Review content'},
            {name: 'Reviewer Name', content: 'Review content'},
            {name: 'Reviewer Name', content: 'Review content'},
            {name: 'Reviewer Name', content: 'Review content'},
            {name: 'Reviewer Name', content: 'Review content'},
            {name: 'Reviewer Name', content: 'Review content'},
            {name: 'Reviewer Name', content: 'Review content'},
            {name: 'Reviewer Name', content: 'Review content'},
            {name: 'Reviewer Name', content: 'Review content'},

        ],
        resumeText: "Resume start here",
        faqs: [
            { question: "What is FAQ?", answer: "FAQ stands for Frequently Asked Questions." },
            { question: "Why use FAQ?", answer: "FAQ sections save time for both customers and service providers." },
            // ... more FAQs
        ]
    });

    const [isEditMode, setIsEditMode] = useState(false);

    const handleProfileUpdate = (updatedProfile) => {
        setTutorProfileData(updatedProfile);
        setIsEditMode(false); // Exit edit mode when update is complete
    };

    const toggleEditMode = () => {
        setIsEditMode(!isEditMode);
    };


    return (
        <div className={styles.pageContainer}>
            <div className={styles.header}>
            </div>
            <div className={styles.mainContent}>
                <div className={styles.leftColumn}>
                    <TutorProfileHeader
                        name={tutorProfileData.name}
                        avatarUrl={tutorProfileData.avatarUrl}
                        subject={tutorProfileData.subject}
                        tagline={tutorProfileData.tagline}
                    />

                    <EditProfile userProfile={tutorProfileData} onUpdate={handleProfileUpdate} onToggleEditMode={toggleEditMode} />

                    {/* visible or invisible */}
                    {!isEditMode && (
                        <>
                            <TutorInfo
                                education={tutorProfileData.highestDegree}
                                school={tutorProfileData.graduatedFrom}
                                birthYear={tutorProfileData.birthYear}
                                certifications={tutorProfileData.certifications}
                                teachingDuration={tutorProfileData.teachingDuration}
                                rating={tutorProfileData.rating}
                            />
                            <TutorIntroduction introText={tutorProfileData.introText}/>
                            <LessonsInformation lessonInfo={tutorProfileData.lessonInfoText}/>
                            <section>
                                <h2>Videos</h2>
                                <VideoGallery videos={tutorProfileData.videos}/>
                            </section>
                            <Reviews reviews={tutorProfileData.reviews}/>
                            <Resume resumeText={tutorProfileData.resumeText}/>
                            <FAQ faqList={tutorProfileData.faqs}/>
                        </>
                    )}
                </div>
                {!isEditMode && (
                    <div className={styles.rightColumn}>
                        <TutorPackages
                            tutorName={tutorProfileData.name}
                            rating={tutorProfileData.rating}
                            trialPrice={tutorProfileData.trailPrice}
                            packages={tutorProfileData.package}/>
                    </div>
                )}
            </div>
        </div>
    );
};

export default TutorProfilePage;