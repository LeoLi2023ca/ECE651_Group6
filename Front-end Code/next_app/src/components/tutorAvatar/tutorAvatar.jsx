import { useState } from 'react';
import Image from 'next/image';
import styles from './tutorAvatar.module.css';

const TutorAvatar = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleMenu = () => {
        setIsOpen(!isOpen);
    };

    return (
        <div className={styles.container} onMouseEnter={toggleMenu} onMouseLeave={toggleMenu}>
            <Image
                src="/avatar.png"
                alt="User Avatar"
                width={40}
                height={40}
                className={styles.avatar}
            />
            {isOpen && (
                <div className={styles.dropdownMenu}>
                    <a href="/tutor-profile">My Profile</a>
                    <a href="/refer-a-friend">Refer a friend</a>
                    <a href="/settings">Settings</a>
                    <a href="/sign-out">Sign Out</a>
                </div>
            )}
        </div>
    );
};

export default TutorAvatar;
