import streamlit as st


st.set_page_config(page_title="Oral Fluency Classification", layout="wide")


if "dataset" not in st.session_state:
	st.session_state.dataset = "Avalinguo"


st.markdown(
	"""
	<style>
	@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

	.stApp {
		background-color: #ececec;
		font-family: 'Inter', sans-serif;
	}

	.block-container {
		max-width: 1120px;
		padding-top: 0;
		padding-bottom: 2.5rem;
	}

	div[data-testid="stVerticalBlock"]:has(.header-bar) {
		gap: 0;
	}

	.header-bar {
		margin-left: -2rem;
		margin-right: -2rem;
		margin-bottom: 3.2rem;
		background: #274d98;
		height: 90px;
		display: flex;
		align-items: center;
		padding-left: 68px;
		border-top: 1px solid #1c3a76;
	}

	.header-title {
		color: #ffffff;
		font-size: 48px;
		font-weight: 800;
		line-height: 1;
		margin: 0;
		letter-spacing: 0.3px;
	}

	.dataset-wrap {
		display: flex;
		justify-content: center;
		align-items: center;
		margin-bottom: 22px;
		gap: 18px;
	}

	.stButton > button {
		border-radius: 999px;
		font-weight: 700;
		font-size: 32px;
		padding: 10px 34px;
		line-height: 1;
		min-height: 0;
		border: 2px solid #2e56a4;
		transition: none;
	}

	.stButton > button[kind="primary"] {
		color: #ffffff;
		background: #2e56a4;
	}

	.stButton > button[kind="secondary"] {
		color: #2e56a4;
		background: #ececec;
	}

	div[data-testid="stFileUploaderDropzone"] {
		border: 2.5px dashed #5a7fc3;
		border-radius: 12px;
		background: #d8deec;
		min-height: 178px;
		display: flex;
		align-items: center;
		justify-content: center;
		padding-top: 0;
	}

	div[data-testid="stFileUploaderDropzone"] section {
		padding: 0;
	}

	div[data-testid="stFileUploaderDropzone"] [data-testid="stFileUploaderDropzoneInstructions"] {
		text-align: center;
		color: #7a7a7a;
	}

	div[data-testid="stFileUploaderDropzone"] [data-testid="stFileUploaderDropzoneInstructions"] div {
		font-size: 18px;
		font-weight: 700;
	}

	div[data-testid="stFileUploaderDropzone"] small {
		font-size: 11px;
		color: #8d8d8d;
	}

	.uploaded-card {
		height: 178px;
		border: 1.8px solid #5a7fc3;
		border-radius: 12px;
		background: #d8deec;
		padding: 22px 24px;
		display: flex;
		align-items: center;
		gap: 20px;
		box-sizing: border-box;
	}

	.audio-icon {
		width: 90px;
		height: 90px;
		border-radius: 12px;
		background: #828282;
		color: #ffffff;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 48px;
		flex-shrink: 0;
	}

	.audio-details {
		flex: 1;
		display: flex;
		flex-direction: column;
		justify-content: center;
		color: #7b7b7b;
	}

	.audio-name {
		font-size: 34px;
		font-weight: 700;
		line-height: 1.1;
		margin: 0 0 8px 0;
	}

	.audio-size {
		font-size: 18px;
		margin: 0;
	}

	.audio-wave {
		font-size: 34px;
		letter-spacing: 2px;
		line-height: 1;
		margin-top: 4px;
		color: #858585;
	}

	.audio-close {
		font-size: 42px;
		color: #8f8f8f;
		margin-left: 8px;
		line-height: 1;
	}

	.arrow-holder {
		margin-top: 44px;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.arrow-circle {
		width: 72px;
		height: 72px;
		border-radius: 50%;
		background: #2e56a4;
		color: #ffffff;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 40px;
		font-weight: 700;
	}

	.result-card {
		border: 2px solid #5a7fc3;
		border-radius: 18px;
		padding: 28px 24px 26px;
		min-height: 415px;
		background: #ececec;
	}

	.result-title-green {
		color: #37c424;
		font-size: 52px;
		font-weight: 800;
		margin: 0 0 22px 0;
		line-height: 1;
	}

	.result-title-red {
		color: #ff1f4e;
		font-size: 52px;
		font-weight: 800;
		margin: 0 0 22px 0;
		line-height: 1;
	}

	.result-text-green {
		color: #37c424;
		font-size: 43px;
		line-height: 1.18;
		font-weight: 500;
		margin: 0;
		text-align: justify;
	}

	.result-text-red {
		color: #ff1f4e;
		font-size: 43px;
		line-height: 1.18;
		font-weight: 500;
		margin: 0;
		text-align: justify;
	}

	@media (max-width: 1200px) {
		.header-title { font-size: 38px; }
		.stButton > button { font-size: 24px; }
		.result-title-green, .result-title-red { font-size: 40px; }
		.result-text-green, .result-text-red { font-size: 30px; }
		.audio-name { font-size: 28px; }
	}
	</style>
	""",
	unsafe_allow_html=True,
)

st.markdown(
	"""
	<div class="header-bar">
		<h1 class="header-title">Oral Fluency Classification</h1>
	</div>
	""",
	unsafe_allow_html=True,
)

side_l, col_left, col_right, side_r = st.columns([2.8, 1.2, 1.2, 2.8], gap="small")

with col_left:
	if st.button(
		"Avalinguo",
		type="primary" if st.session_state.dataset == "Avalinguo" else "secondary",
		use_container_width=True,
	):
		st.session_state.dataset = "Avalinguo"

with col_right:
	if st.button(
		"SpeechOcean",
		type="primary" if st.session_state.dataset == "SpeechOcean" else "secondary",
		use_container_width=True,
	):
		st.session_state.dataset = "SpeechOcean"

top_left, top_right = st.columns([12, 1.4], gap="small")

with top_left:
	uploaded_audio = st.session_state.get("uploaded_audio_obj")

	if uploaded_audio is None:
		uploaded_audio = st.file_uploader(
			"Upload speech audio",
			type=["wav", "mp3"],
			label_visibility="collapsed",
			key="audio_uploader",
		)
		if uploaded_audio is not None:
			st.session_state.uploaded_audio_obj = uploaded_audio
			st.rerun()

	if uploaded_audio is not None:
		size_mb = uploaded_audio.size / (1024 * 1024)
		st.markdown(
			f"""
			<div class="uploaded-card">
				<div class="audio-icon">♪</div>
				<div class="audio-details">
					<p class="audio-name">{uploaded_audio.name}</p>
					<p class="audio-size">{size_mb:.1f} MB</p>
					<div class="audio-wave">◉||| ||| |||| ||| || ||| |||| |||| ||||| ..............</div>
				</div>
				<div class="audio-close">⊗</div>
			</div>
			""",
			unsafe_allow_html=True,
		)

with top_right:
	st.markdown(
		"""
		<div class="arrow-holder">
			<div class="arrow-circle">➜</div>
		</div>
		""",
		unsafe_allow_html=True,
	)

st.markdown("<div style='height:28px;'></div>", unsafe_allow_html=True)

bottom_left, bottom_right = st.columns(2, gap="large")

with bottom_left:
	st.markdown(
		"""
		<div class="result-card">
			<h2 class="result-title-green">Baseline SVM</h2>
			<p class="result-text-green">
				The features are mapped into a higher-dimensional space using a non-linear kernel,
				where similarity relationships between samples are computed. A quadratic programming
				solver then identifies key support vectors and determines the decision boundary,
				which is used to classify speech samples into their corresponding fluency categories.
			</p>
		</div>
		""",
		unsafe_allow_html=True,
	)

with bottom_right:
	st.markdown(
		"""
		<div class="result-card">
			<h2 class="result-title-red">Proposed SVM</h2>
			<p class="result-text-red">
				These features are mapped into a hybrid feature space using Random Fourier Features
				and the Nyström method to efficiently represent non-linear speech patterns.
				The resulting features are then passed to an SVM classifier trained using Sequential
				Minimal Optimization, which enables efficient model training. The trained model
				classifies the input speech into its corresponding oral fluency category.
			</p>
		</div>
		""",
		unsafe_allow_html=True,
	)
