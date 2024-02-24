import styles from "./tutorPost.module.css";
import TutorPostBtnPage from "./tutorPostBtn/tutorPostBtn";

const TutorPost = () => {
  return (
    <div className={styles.container}>
      <div>
        <TutorPostBtnPage />
      </div>
    </div>
  )
};

export default TutorPost;
