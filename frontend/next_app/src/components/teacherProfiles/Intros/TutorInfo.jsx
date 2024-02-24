// components/TutorInfo.jsx
import styles from './TutorInfo.module.css';

const TutorInfo = ({ education, school, birthYear, certifications, teachingDuration, rating }) => (
    <div className={styles.container}>
        <div className={styles.info}>
            <strong>Highest Degree:</strong> {education}
        </div>
        <div className={styles.info}>
            <strong>Graduated From:</strong> {school}
        </div>
        <div className={styles.info}>
            <strong>Year of Birth:</strong> {birthYear}
        </div>
        <div className={styles.certifications}>
            <strong>Certifications:</strong> {certifications.join(', ')}
        </div>
        <div className={styles.info}>
            <strong>Teaching Hours:</strong> {teachingDuration} hours
        </div>
        <div className={styles.rating}>
            <strong>Teacher Rating:</strong> {rating} / 5
        </div>
    </div>
);

export default TutorInfo;
