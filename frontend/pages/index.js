import { useEffect, useState } from "react";

export default function Home() {
  const [questions, setQuestions] = useState([]);
  const [filtered, setFiltered] = useState([]);
  const [selected, setSelected] = useState(null);
  const [answer, setAnswer] = useState(null);
  const [showExplanation, setShowExplanation] = useState(false);

  const [topic, setTopic] = useState("All");
  const [level, setLevel] = useState("All");
  const [timer, setTimer] = useState(60);

  useEffect(() => {
    fetch("http://localhost:8000/api/v1/questions/")
      .then((res) => res.json())
      .then((data) => {
        setQuestions(data);
        setFiltered(data);
      })
      .catch((err) => console.error(err));
  }, []);

  // Reset timer whenever new question is shown
  useEffect(() => {
    let countdown;
    if (selected !== null && timer > 0) {
      countdown = setInterval(() => setTimer((t) => t - 1), 1000);
    }
    return () => clearInterval(countdown);
  }, [selected, timer]);

  const handleFilter = () => {
    let q = questions;
    if (level !== "All") q = q.filter((x) => x.level === level);
    if (topic !== "All") q = q.filter((x) => x.topic === topic);
    setFiltered(q);
    setSelected(null);
    setAnswer(null);
    setShowExplanation(false);
    setTimer(60);
  };

  const handleAnswer = (choice) => {
    setAnswer(choice);
    setShowExplanation(true);
  };

  const nextQuestion = () => {
    if (filtered.length > 0) {
      const random = filtered[Math.floor(Math.random() * filtered.length)];
      setSelected(random);
      setAnswer(null);
      setShowExplanation(false);
      setTimer(60);
    }
  };

  return (
    <div className="layout">
      {/* Top Filters */}
      <div className="filters">
        <select value={level} onChange={(e) => setLevel(e.target.value)}>
          <option value="All">All Levels</option>
          <option value="L1">Level 1</option>
          <option value="L2">Level 2</option>
          <option value="L3">Level 3</option>
        </select>
        <select value={topic} onChange={(e) => setTopic(e.target.value)}>
          <option value="All">All Topics</option>
          {Array.from(new Set(questions.map((q) => q.topic))).map((t) => (
            <option key={t} value={t}>{t}</option>
          ))}
        </select>
        <button onClick={handleFilter}>Apply</button>
        <button onClick={nextQuestion}>Next Question</button>
      </div>

      {/* Grid Body */}
      <div className="grid">
        {/* Left Column - Ads */}
        <div className="ads">
          <p>[Ad Slot]</p>
        </div>

        {/* Middle Column - Question */}
        <div className="question">
          {selected ? (
            <>
              <h3>{selected.topic} ({selected.level})</h3>
              <p>{selected.stem}</p>
              <div className="choices">
                {selected.choices.map((choice, i) => (
                  <button
                    key={i}
                    onClick={() => handleAnswer(choice)}
                    disabled={!!answer}
                  >
                    {choice}
                  </button>
                ))}
              </div>
              <p className="timer">Time left: {timer}s</p>
            </>
          ) : (
            <p>Click "Next Question" to start.</p>
          )}
        </div>

        {/* Right Column - Explanation */}
        <div className="explanation">
          {showExplanation && selected && (
            <>
              <h4>Explanation</h4>
              <p>{selected.explanation}</p>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
