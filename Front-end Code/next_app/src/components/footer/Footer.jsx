import styles from "./footer.module.css";
import ScBtn from "./button/scBtn";
import Links from "./links/Links";

const Footer = () => {
  return (
    <div className={styles.container}>
      <div>
        <Links />
      </div>
      <ScBtn />
    </div>
  )
};

export default Footer;


// return (
//   <div className={styles.container}>
//     <div className={styles.logo}>Back to the top</div>

//     <div className={styles.text}>
//       Back to top
//     </div>
//   </div>
// );