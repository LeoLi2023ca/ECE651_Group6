import styles from "./studentMyPost.module.css"
import PostList from "@/components/postComponents/postList";


const StudentMyPostPage = () => {
    return (
        <div className={styles.container}>
           <PostList/>
        </div>
    )

};

export default StudentMyPostPage;