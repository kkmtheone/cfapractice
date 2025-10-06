import { useRouter } from "next/router";

export default function QuizPage() {
  const router = useRouter();
  const { id } = router.query;

  return (
    <div>
      <h1>Quiz Page</h1>
      <p>Quiz ID: {id}</p>
    </div>
  );
}
