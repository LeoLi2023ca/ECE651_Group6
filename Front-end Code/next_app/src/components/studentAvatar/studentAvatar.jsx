import { useState } from 'react';
import Image from 'next/image';
import styles from './studentAvatar.module.css';

const StudentAvatar = () => {
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
                    <a href="/student-profile">My Profile</a>
                    <a href="/refer-a-friend">Refer a friend</a>
                    <a href="/settings">Settings</a>
                    <a href="/sign-out">Sign Out</a>
                </div>
            )}
        </div>
    );
};

export default StudentAvatar;
