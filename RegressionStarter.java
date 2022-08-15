public class RegressionStarter {
    public static void main(String args[]) {
        double[] inputs = new double[] { 100, 316, 1000, 3162, 10000, 31622, 100000 };
        double[] expected = new double[] { 9795,	20885,	55760,	188397,	707632,	2880331,	8943890};
        NLogNRegression regression = new NLogNRegression(inputs, expected);
        // QuadraticRegression regression = new QuadraticRegression(inputs, expected);
        System.out.println("R^2: " + regression.rSquared());
    }
}