import styles from "./studentPost.module.css";
import StudentPostBtnPage from "./studentPostBtn/studentPostBtn";

const StudentPost = () => {
  return (
    <div className={styles.container}>
      <div>
        <StudentPostBtnPage />
      </div>
      {/* <div className={styles.post}>
        <StudentMyPostPage />
      </div> */}
    </div>
  )
};

export default StudentPost;
