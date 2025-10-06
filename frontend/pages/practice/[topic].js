import { useRouter } from "next/router";

export default function PracticePage() {
  const router = useRouter();
  const { topic } = router.query;

  return (
    <div>
      <h1>Practice Page</h1>
      <p>Topic: {topic}</p>
    </div>
  );
}
