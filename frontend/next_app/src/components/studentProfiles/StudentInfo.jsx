
import styles from './StudentInfo.module.css';

const StudentInfo = ({ education, school, grade, studyTime, email, time }) => (
    <div className={styles.container}>
        <div className={styles.info}>
            <strong>Current education:</strong> {education}
        </div>
        <div className={styles.info}>
            <strong>Current School:</strong> {school}
        </div>
        <div className={styles.info}>
            <strong>Current grade:</strong> Grade {grade}
        </div>
        <div className={styles.info}>
            <strong>Except Study time:</strong> {studyTime} hours
        </div>
        <div className={styles.rating}>
            <strong>Email:</strong> {email}
        </div>
        <div className={styles.rating}>
            <strong>Time Zone:</strong> {time}
        </div>
    </div>
);

export default StudentInfo;
